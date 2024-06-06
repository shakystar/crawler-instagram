import os
import time
from selenium import webdriver

import instagram
import json_data
from setting import *

targets = [
    ("https://www.instagram.com/s.t___kim/", ACCOUNT),
    ("https://www.instagram.com/explore/tags/논픽션", KEYWORD),
]

results = []

if not os.path.exists(OUTPUT_FOLDER):
    os.mkdir(OUTPUT_FOLDER)

driver = webdriver.Chrome()

instagram.login(driver)

for url, mode in targets:
    url:str = url

    driver.get(url)
    current_url = driver.current_url

    time.sleep(7)
    if mode == ACCOUNT:
        instagram.select_account_first(driver)
    elif mode == KEYWORD:
        instagram.select_search_first(driver)
    else:
        print("wrong mode...;")
        break

    while 1:
        if current_url == driver.current_url: 
            break
        else:
            current_url = driver.current_url

        content = instagram.get_content(driver)

        if content:
            results.append(content)
        else:
            break
        
        instagram.move_next(driver)
    
    output_path = json_data.get_output_path(url)
    cleaned_data = json_data.clean_data(results, save=True, output_path=output_path+".json")
    json_data.json_to_excel(cleaned_data, output_path=output_path+".xlsx")

print("end...!")