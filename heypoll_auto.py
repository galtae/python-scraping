from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from time import sleep
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
# options.add_argument('headless')
# options.add_argument('window-size=1920x1080')
# options.add_argument('diable=gpu')
options.add_experimental_option("detach", True)
#browser = webdriver.Chrome()
driver = webdriver.Chrome('./chromedriver.exe', options=options)

def attendance_check():

    url_path = 'https://www.heypoll.co.kr/event/main/view/920'
    driver.get(url_path)
    try:
        driver.find_element(By.CLASS_NAME, "today").click()
    except Exception as x:
        print(x)


if __name__ == "__main__":
    driver.get('https://www.heypoll.co.kr/login')

    sleep(0.5)
    driver.find_element(By.ID, "email").send_keys(id)
    driver.find_element(By.ID, "password").send_keys(pass)
    driver.find_element(By.CLASS_NAME, "login-submit").click()
    sleep(3)

    # 출석체크
    attendance_check()
    exit(1)

    poll_url = 'https://www.heypoll.co.kr/poll'
    driver.get(poll_url)
    sleep(3)

    for i in range(0, 2000):
        try:
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            result = driver.find_element(By.CLASS_NAME, 'close-modal')
            result.click()
            sleep(0.5)

            # 항목 선택
            '''
            result = driver.find_element(By.XPATH, '//*[@id="polls"]/li[' + str(i) + ']/div/div[2]/div[7]')
            result.click()
            sleep(0.5)
            '''

            result = driver.find_element(By.XPATH, '//*[@id="polls"]/li[' + str(i) + ']/div/div[2]/div[7]/div')
            result.click()
            sleep(0.5)

            # 투표 참여
            #result = driver.find_element(By.CSS_SELECTOR, 'polls > li:nth-child(1) > div > div.btn-group > a.btn.btn-wide.btn-primary')
            result = driver.find_element(By.XPATH, '//*[@id="polls"]/li[' + str(i) + ']/div/div[5]/a[1]')
            result.click()
            sleep(0.5)

            result = driver.find_element(By.CLASS_NAME, 'close-modal')
            result.click()
            sleep(0.5)

            result = driver.find_element(By.CLASS_NAME, 'close-modal')
            result.click()
            sleep(0.5)

        except Exception as x:
            continue