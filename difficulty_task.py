import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
try:
    driver=webdriver.Chrome()
    for i in range(1,11):
        driver.get('https://mathup.com/games/crossbit?mode=championship')
        driver.maximize_window()
        wait=WebDriverWait(driver,60)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div[text()='Start']"))).click()
        level=wait.until(expected_conditions.presence_of_element_located((By.XPATH,'//div[@class="GamePostStart_basic-info-wrapper__IGqxn"]/div[2]/div[1]/div[2]/div[2]'))).text
        print(f'execution {i} : '+level)
    driver.quit()
except Exception as e:
    print(f'Error while running script : {e}')