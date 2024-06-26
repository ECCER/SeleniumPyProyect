from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('D:\WebDrivers\chromedriver-win64\chromedriver.exe')


driver = webdriver.Chrome(service=service)

driver.get("http://selenium.dev")

print(driver.title)

driver.quit()