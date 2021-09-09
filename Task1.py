from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='C://Program Files//chromedriver//chromedriver.exe')
link = ["https://noobtest.id","https://erzaf.com","https://orangsiber.com","https://demoqa.com","https://automatetheboringstuff.com"]
driver.minimize_window()

for i in link:
    driver.get(i)
    print(driver.title)
    
driver.close()
