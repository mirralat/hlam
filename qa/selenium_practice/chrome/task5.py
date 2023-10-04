from selenium import webdriver
import time
import pickle

options = webdriver.ChromeOptions()
options.add_argument('Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0')

browser = webdriver.Chrome('chromedriver.exe', options=options)
url = 'https://vk.com'

try:
    browser.get(url=url)
    time.sleep(5)
    username_input = browser.find_element('index_email')
    username_input.send_keys('test')
    button = browser.find_element('index_login_button').click()

    pickle.dump(browser.get_cookies(), open('cookies', 'wb'))

except Exception as ex:
    print(ex)

finally:
    browser.close()
    browser.quit()
