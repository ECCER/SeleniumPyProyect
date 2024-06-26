import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service('D:\WebDrivers\chromedriver-win64\chromedriver.exe')


driver = webdriver.Chrome(service=service)

driver.get("http://demoqa.com/text-box")
driver.maximize_window()
time.sleep(2)

nom = driver.find_element(By.XPATH, "//input[contains(@id, 'userName')]")
nom.send_keys("Eccer")
time.sleep(2)

driver.quit()