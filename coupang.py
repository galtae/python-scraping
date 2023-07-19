import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from time import sleep
import subprocess
import shutil
import clipboard

subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"')

options = webdriver.ChromeOptions()

# options.add_argument('headless')
# options.add_argument('window-size=1920x1080')
# options.add_argument('diable=gpu')
#options.add_experimental_option("detach", True)
#options.add_argument("headless")
#browser = webdriver.Chrome()

options.add_argument("--disable-blink-features=AutomationControlled")
user_ag = UserAgent().random
options.add_argument('user-agent=%s'%user_ag)
options.add_experimental_option("excludeSwitches", ["enable-automation"])

options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("prefs", {"prfile.managed_default_content_setting.images": 2})
#driver = webdriver.Chrome('./chromedriver.exe', options=options)
#driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": """ Object.defineProperty(navigator, 'webdriver', { get: () => undefined }) """})
'''
options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome('c:\\chromedriver.exe', chrome_options=options)
driver.implicitly_wait(3)
'''

options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome('c:\\chromedriver.exe', chrome_options=options)
driver.implicitly_wait(3)
# url = 'https://login.coupang.com/login/login.pang?rtnUrl=https%3A%2F%2Fwww.coupang.com%2Fnp%2Fpost%2Flogin%3Fr%3Dhttps%253A%252F%252Fwww.coupang.com%252F'
# driver.get(url)

id = 'galtae@naver.com'
password = '~!Nlplab315'

if __name__ == "__main__":

    search_url = 'https://partners.coupang.com/#affiliate/ws/link/0/'    
    search_term = 'water'
    driver.get(search_url + search_term)    
    sleep(1.5)
    # 로그인 창이 뜨면
    if driver.current_url.find('login') != -1:
        #driver.find_element(By.XPATH, '//*[@id="login-email-input"]').send_keys(id)
        #driver.find_element(By.XPATH, '//*[@id="login-password-input"]').send_keys(password)
        xpath1 ='/html/body/div[1]/div[1]/div[2]/div[1]/form/div[5]/button'
        xpath2 = '/html/body/div[1]/div[1]/div[1]/div/form/div[5]/button'
        try:
            result = driver.find_element(By.XPATH, xpath1) 
            result.click()
        except Exception as E:
            result = driver.find_element(By.XPATH, xpath2) 
            result.click()
     
    # 검색 결과에서 첫 번째 제품의 이름과 링크 가져오기
    sleep(1.5)
    product_name = ''
    product_link = ''
    #xpath1 = '//*[@id="root"]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/section[3]/div/div[2]/div/div/div/div[1]/div[1]/div[1]/img'
    '''
    for i in range(1, 5):
        xpath = '//*[@id="root"]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/section[3]/div/div[2]/div/div/div/div[1]/div[' + str(i) + ']/div[1]/img'
        product_name = driver.find_element(By.XPATH, xpath).text
        print("first name:", product_name)
        print("first link:", product_link)
    '''

    
    xpath_product_main = '//*[@id="root"]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/section[3]/div/div[2]/div/div/div/div[1]/div[1]/div[1]/img'    
    xpath_pruduct_gen_url = '//*[@id="root"]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/section[3]/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/button[2]'
    product_name = driver.find_element(By.XPATH, xpath_product_main).click()
    sleep(2)
    product_name = driver.find_element(By.XPATH, xpath_pruduct_gen_url).click()
    sleep(2)

    ### 링크 생성 페이지에서 url 복사 버튼 클릭
    xpath_url_cpy_btn = '//*[@id="root"]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div/div[2]/div/div/div/section/section[1]/div/div/div[2]/button'
    product_name = driver.find_element(By.XPATH, xpath_url_cpy_btn).click()    
    # print(clipboard.paste())
    driver.back()
    sleep(2)
    product_name = driver.find_element(By.XPATH, xpath_product_main).click()
    sleep(2)
    
    xpath_pruduct_goto = '//*[@id="root"]/div/div/div[2]/div/div/div[1]/div/div/div[2]/div/div/div/div/div/div/section[3]/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/button[1]'
    product_name = driver.find_element(By.XPATH, xpath_pruduct_goto).click()

    ### 제품 정보 페이지
    sleep(1)
    driver.switch_to.window(driver.window_handles[1])  
    xpath_product_name = '//*[@id="contents"]/div[1]/div/div[3]/div[3]/h2'
    class_product_name = 'prod-buy-header__title'
    xpath_product_price = '//*[@id="contents"]/div[1]/div/div[3]/div[5]/div[1]/div/div[3]/span[1]/strong'
    xpath_product_img = '//*[@id="repImageContainer"]/img'
    class_product_img = 'prod-image__detail'
    result_name = product_name = driver.find_element(By.CLASS_NAME, class_product_name).text
    result_price = product_name = driver.find_element(By.XPATH, xpath_product_price).text
    result_img_src = driver.find_element(By.CLASS_NAME, class_product_img)
    

    print(result_name)
    print(result_price)
  
    # 결과 출력
    #print("first name:", product_name)
    #print("first link:", product_link)
