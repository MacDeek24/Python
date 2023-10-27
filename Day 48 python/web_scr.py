from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chromedriver_path = "C:\\Development\\chromedriver-win64\\chromedriver.exe"

service = Service(executable_path=chromedriver_path)

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

product_url = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(product_url)


event_count = driver.find_elements(By.CSS_SELECTOR , "#articlecount a")
# for event in event_count:
print(event_count[0].text)

driver.quit()
