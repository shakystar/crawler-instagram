import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from setting import USERNAME, PASSWORD

login_url = "https://www.instagram.com/accounts/login/"

xpath_login_section = '//*[@id="loginForm"]/div/div[3]'

xpath_account_post_front = "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/div[2]/div"

xpath_search_post_front  = "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/article/div/div[2]/div"

content_xpaths = [
    "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/div[1]/li",
    '/html/body/div[7]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/div[1]/li',
    '/html/body/div[8]/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/div[1]/ul/div[1]/li'
]

def login(driver:webdriver.Chrome):
    driver.get(login_url)
    time.sleep(3) 

    elem_login = driver.find_element(By.NAME, "username")
    elem_login.clear()
    elem_login.send_keys(USERNAME)

    elem_login = driver.find_element(By.NAME, 'password')
    elem_login.clear()
    elem_login.send_keys(PASSWORD)
    time.sleep(1)

    driver.find_element(By.XPATH, xpath_login_section).click()
    time.sleep(4)

def select_account_first(driver:webdriver.Chrome):
    try:
        right = driver.find_element(By.XPATH, xpath_account_post_front + f"/div[1]/div[1]/a")
    except NoSuchElementException:
        try:
            right = driver.find_element(By.XPATH, xpath_account_post_front + f"/div/div[1]/a") # row only one.
        except:
            driver.get(driver.current_url)
            time.sleep(7)
            if not select_account_first(driver):
                print("error: none post. edit xpath. or retry.")
                time.sleep(1000)
    right.click()
    time.sleep(3)
    return True

def select_search_first(driver:webdriver.Chrome):
    right = driver.find_element(By.XPATH, xpath_search_post_front + f"/div[1]/div[1]/a")
    right.click()
    time.sleep(3)

def move_next(driver:webdriver.Chrome):
    try:
        body = driver.find_element(By.TAG_NAME, 'body')
        body.send_keys(Keys.ARROW_RIGHT)
        time.sleep(2)
        return 1
    except:
        print("error: none next. edit xpath.")
        time.sleep(1000)

def get_content(driver:webdriver.Chrome):    
    for xpath in content_xpaths:
        try:
            element = driver.find_element(By.XPATH, xpath)
            html_source = element.get_attribute('outerHTML')
            time.sleep(1)
            return html_source
        except:
            pass

    print("error: none content. edit xpath.")
    time.sleep(1000)
    return None
