from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def screenshot(d,path):
    name=path+'\screenshots'+'\screenshot_'+time.asctime().replace(':','_')+'.png'
    print(name)
    d.save_screenshot(name)
driver=webdriver.Chrome()
driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_prompt")
driver.maximize_window()
driver.implicitly_wait(2)
f1=driver.find_element(By.XPATH,'//iframe[@id="iframeResult"]')
driver.switch_to.frame(f1)
# screenshot(driver,r'C:\Users\tilak\PycharmProjects\Selenium')
driver.save_screenshot(r"C:\Users\tilak\PycharmProjects\Selenium\screenshots\ss1.png")
element=driver.find_element(By.XPATH,"//h1[text()='The Window Object']")
driver.execute_script("arguments[0].style.border='3px solid red'", element)
# screenshot(driver,r'C:\Users\tilak\PycharmProjects\Selenium')
driver.save_screenshot(r'C:\Users\tilak\PycharmProjects\Selenium\screenshots\ss2.png')
time.sleep(2)
