from selenium import webdriver
import pytest,time
from selenium.webdriver.common.by import By


def data():
    return [
        ('abc@xyz.com','qwert'),
        ('def@xyz.com','yuiop'),
        ('ghi@xyz.com','asdfg')
    ]

def setup_function():
    global driver
    driver = webdriver.Chrome()
    driver.get('https://www.facebook.com/')
    driver.maximize_window()

def teardown_function():
    driver.quit()

@pytest.mark.parametrize('username,password',data())
def test_login(username,password):
    print(username+'---'+password)
    driver.find_element(By.XPATH,'//input[@id="email"]').send_keys(username)
    driver.find_element(By.XPATH,'//input[@id="pass"]').send_keys(password)
    time.sleep(1)

