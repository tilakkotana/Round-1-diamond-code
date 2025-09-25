from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.way2automation.com/angularjs-protractor/webtables/")
driver.maximize_window()
driver.implicitly_wait(2)
rows=driver.find_elements(By.XPATH,'//tbody/tr')
total_rows=len(rows)
cols=driver.find_elements(By.XPATH,'//thead/tr[3]/th')
total_cols=len(cols)
print('total_rows='+str(total_rows)+' total_cols='+str(total_cols))
for row in rows:
    print(row.text)
print("-----------------------------------------------------------------")
for i in range(1,total_rows+1):
    for j in range(1,total_cols):
        print(driver.find_element(By.XPATH,f'//tbody/tr[{i}]/td[{j}]').text,end=' ')
    print()


