from selenium import webdriver
import time


options = webdriver.ChromeOptions()
options.add_argument('Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0')
options.add_argument('--disable0blink-features=AutomationControlled')
browser = webdriver.Chrome('chromedriver.exe', options=options)
url = 'https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html'

try:
    browser.get(url=url)
    time.sleep(20)

except Exception as ex:
    print(ex)

finally:
    browser.close()
    browser.quit()
