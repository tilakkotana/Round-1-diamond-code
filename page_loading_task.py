import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

try:
    times=[]
    driver=webdriver.Chrome()
    for i in range(1,11):
        start=time.time()
        driver.get("https://mathup.com/games/crossbit?mode=daily_challenge")
        driver.maximize_window()
        wait=WebDriverWait(driver,60)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div[text()='Start']")))
        end=time.time()
        t=end-start
        times.append(t)
        print(f'execution {i} : {t} seconds')
    avg_time=sum(times)/len(times)
    print(f'average time : {avg_time} seconds')
    print(f'average time rounded : ',round(avg_time,2),' seconds')
except Exception as e:
    print(f'Error while running script - {e}')

