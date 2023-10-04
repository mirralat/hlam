

# David Beazley
# 2015 PyCon
import socket
from select import select

tasks = []	# очередь для event loop, сюда кладем генераторы


to_read = {}	# сокеты и генераторы для чтения
to_write = {}	# сокеты для записи




def server():
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_socket.bind(('localhost', 5001))


	while True:
		
		yield ('read', server_socket)	# отдаем серверный сокет
		# перед тем как вызывается блокирующий метод генератор выдает кортеж с сокетом
		client_socket, addr = server_socket.accept()	# read
		print('Connection from', addr)
		tasks.append(client(client_socket))	# добавим клиентский сокет в список tasks


def client(client_socket):
	while True:
		yield ('read', client_socket)
		request = client_socket.recv(4096)	# read

		if not request:
			break
		else:
			responce = 'Hello world\n'.encode()
			yield ('write', client_socket)
			client_socket.send(responce)	# write

	print('Outside inner while loop')
	client_socket.close()



def event_loop():
	# ключ сокет объект генератор
	while any([tasks, to_read, to_write]):	# принимаем список, если хоть какой-то True, то вернет True, пустой словарь - Fakse

		while not tasks:
			read_to_read, ready_to_write = select(to_read, to_write, [])	# селект возьмет ключи

			# нужно для того чтобы event_loop Постоянно работал
			for sock in ready_to_read:
				tasks.append(to_read.pop(socket))	# берем ключ-сокет

			for sock in ready_to_write:
				tasks.append(to_write.pop(socket))	# обеспечиваем проход по кругу

		try:
			task = tasks.pop(0)

			reason, sock = next(task)	# передаем сюда генератор

			if reason == 'read':
				to_read[sock] = task
			if reason == 'write':
				to_write[sock] = task
		except StopIteration:
			print('Done')


tasks.append(server())
event_loop()



'''

Функции преобразованы в генераторы. Генераторы передают кортеж, где первый элемент фильтрующий признак, по которому
определяется, куда пойдет элемент кортежа (чтение/запись). Отдает в event loop, где происходит получение генератора и вызов
next() с аргументом task. На выходе получается кортеж.
Дальше идет сравнение, если write, to словарь  write пополняем парой ключа со значением. Ключ - сокет, значение - объект генератора.
Словари to_read и to_write таким образом пополняются генераторами. 
Tasks - конечная структура, он не будет наполняться вечно. Очередь задач должна пополняться, а вложенный while нужен для ее заполнения.
В select передаются словари, откуда берутся ключи. Select получает ключ-сокет, делается выборка читающих и записывающих через select. В каждом
for обрабатываются эти случаи. Метод pop отдает из словаря значение ключа по сокету.

Генераторы отработали потому что перед тем как вызвать блокирующие операции, передавалось управление с yield в event loop. В событийном цикле
прошла выборка, блокирующие функции не мешали работе
'''