from selenium import webdriver
import time

browser = webdriver.Chrome('chromedriver.exe')

url = 'https://google.com'

try:
    browser.get(url=url)
    time.sleep(5)
    browser.refresh()

except Exception as ex:
    print(ex)

finally:
    browser.close()
    browser.quit()
