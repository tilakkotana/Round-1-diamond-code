from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get("https://accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ifkv=AfYwgwW2_XIuKCYlw5dA18NBeVi84nIGg0LuHF46JEj-1hyUh7NwStxveH55VkGbwJ9uNL1a_dqZrw&osid=1&passive=1209600&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-2111649345%3A1758175509903818")
driver.maximize_window()
driver.find_element(By.XPATH,'//input[@type="email"]').send_keys('tilakkotana25007@gmail.com')
wait=WebDriverWait(driver,45)
wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"//*[@class=\"O1Slxf\"]/div[1]"))).click()