from selenium import webdriver
import time
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('window-size=1920x1080')
# options.add_argument('diable=gpu')
options.add_argument('Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36')
options.add_argument('lang=ko_KR')

driver = webdriver.Chrome('./chromedriver.exe', chrome_options=options)
driver.implicitly_wait(3)
driver.get('https://ko-kr.facebook.com/')


id = ''
password = ''

driver.find_element_by_id('email').send_keys(id)

driver.find_element_by_id('pass').send_keys(password)

driver.find_element_by_css_selector('#login_form > table > tbody > tr:nth-child(2) > td:nth-child(3) > label > input[type=submit]').click()

time.sleep(3)

driver.get('https://www.facebook.com/find-friends/browser/')
time.sleep(3)

html = driver.page_source
soup = BeautifulSoup(html)

driver.get_screenshot_as_file('aaa.png')

time.sleep(5)

print(soup)

#driver.close()
