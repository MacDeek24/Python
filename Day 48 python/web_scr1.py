from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chromedriver_path = "C:\\Development\\chromedriver-win64\\chromedriver.exe"

service = Service(executable_path=chromedriver_path)

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

product_url = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(product_url)

cookie = driver.find_element(By.ID ,"cookie")
