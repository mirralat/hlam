from selenium import webdriver
import time

url = 'https://2ip.ru/'

options = webdriver.ChromeOptions()
options.add_argument('--proxy-server=200.198.42.168:8080')     # меняем user-agent
browser = webdriver.Chrome('chromedriver.exe', options=options)
browser.get(url)


try:
    browser.get(url=url)
    time.sleep(5)
    browser.refresh()

except Exception as ex:
    print(ex)

finally:
    browser.close()
    browser.quit()
