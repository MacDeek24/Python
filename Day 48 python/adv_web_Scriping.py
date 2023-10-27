from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chromedriver_path = "C:\\Development\\chromedriver-win64\\chromedriver.exe"

service = Service(executable_path=chromedriver_path)

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

product_url = "https://www.amazon.in/dp/B0BGS67H69/ref=sspa_dk_detail_1?psc=1&pd_rd_i=B0BGS67H69&pd_rd_w=SV2Dq&content-id=amzn1.sym.2575ab02-73ff-40ca-8d3a-4fbe87c5a28d&pf_rd_p=2575ab02-73ff-40ca-8d3a-4fbe87c5a28d&pf_rd_r=73BVD4E2ZWXVYJEC2RKB&pd_rd_wg=ijjpQ&pd_rd_r=93aee7b8-3f71-4ec7-a586-f9841f956e1d&s=shoes&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw"
driver.get(product_url)


elements = driver.find_elements(By.CLASS_NAME, 'a-price-whole')
for element in elements:
    print(element.text)

driver.quit()
