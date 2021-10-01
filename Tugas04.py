from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path='C://Program Files//chromedriver//chromedriver.exe')


link = "https://demoqa.com/text-box"
driver.get(link)
driver.maximize_window()

driver.find_element_by_id('userName').send_keys("Suseno")
driver.find_element_by_id('userEmail').send_keys("uno@noobtest.id")
driver.find_element_by_id('currentAddress').send_keys("Surabaya")
driver.find_element_by_id('permanentAddress').send_keys("Mulyos")
element = driver.find_element_by_id('submit')


#driver.close()
