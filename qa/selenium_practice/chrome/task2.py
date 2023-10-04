from selenium import webdriver
import time

url = 'https://www.whatsmyua.info/'

agents = ['	Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.81 Mobile Safari/537.36',
          'Mozilla/5.0 (iPhone; CPU iPhone OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.1 Mobile/15E148 Safari/604.1',
          '	Mozilla/5.0 (iPad; CPU OS 14_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1',
          'Test']

for data in agents:
    options = webdriver.ChromeOptions()
    options.add_argument(f'user-agent={data}')     # меняем user-agent
    browser = webdriver.Chrome('chromedriver.exe', options=options)

    try:
        browser.get(url=url)
        time.sleep(5)
        browser.refresh()

    except Exception as ex:
        print(ex)

    finally:
        browser.close()
        browser.quit()
