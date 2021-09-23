from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome(executable_path='C://Program Files//chromedriver//chromedriver.exe')

#driver.minimize_window
driver.get('https://demoqa.com/alerts')
try:
    driver.find_element_by_id('timerAlertButton').click()
    WebDriverWait(driver,6).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    print("Button 5 detik berhasil di klik")
except TimeoutException:
    print("Button 5 detik gagal di klik")
    pass
driver.close()
    
