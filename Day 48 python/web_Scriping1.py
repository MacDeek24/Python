from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chromedriver_path = "C:\\Development\\chromedriver-win64\\chromedriver.exe"

service = Service(executable_path=chromedriver_path)

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

product_url = "https://www.python.org/"
driver.get(product_url)


event_time = driver.find_elements(By.CSS_SELECTOR , ".event-widget time")
event_name = driver.find_elements(By.CSS_SELECTOR , ".event-widget li a")
event = {}

for n in range (len(event_time)):
    event[n]={
        'Time': event_time[n].text,
        'Name': event_name[n].text
    }

print(event)

driver.quit()
