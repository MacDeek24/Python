from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import time


zillow_url = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Atrue%2C%22mapBounds%22%3A%7B%22west%22%3A-122.70318068457031%2C%22east%22%3A-122.16347731542969%2C%22south%22%3A37.703343724016136%2C%22north%22%3A37.847169233586946%7D%2C%22mapZoom%22%3A11%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22price%22%3A%7B%22min%22%3Anull%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3Anull%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%2C%22max%22%3Anull%7D%7D%2C%22isListVisible%22%3Atrue%7D"


chrome_driver_path = "C:\\Development\\chromedriver-win64\\chromedriver.exe"


address_xpath = '//*[@id="zpid_37.806293--122.266235"]/div/div[1]/a/address"]'
price_xpath = '//*[@id="zpid_37.806293--122.266235"]/div/div[1]/div[2]/div/span"]'
link_xpath = '//*[@id="logono"]/div[2]/div/div/a"]'
submit_button_xpath = '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div"]'


header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}
response = requests.get(zillow_url, headers=header)
data = response.text
soup = BeautifulSoup(data, "html.parser")


all_link_elements = soup.find_all("address")
all_links = [f"https://www.zillow.com{link['href']}" if 'http' not in link['href'] else link['href'] for link in all_link_elements]
all_address_elements = soup.select('address[data-test="property-card-addr"]')
all_addresses = [address.get_text().split(" | ")[-1] for address in all_address_elements]
all_price_elements = soup.select(".list-card-heading")
all_prices = []

print(all_addresses)

for element in all_price_elements:
    try:
        price = element.select(".list-card-price")[0].text
    except IndexError:
        print('Multiple listings for the card')
        price = element.select(".list-card-details li")[0].text
    all_prices.append(price)


chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
driver = webdriver.Chrome(service=ChromeService(executable_path=chrome_driver_path), options=chrome_options)


for n in range(len(all_links)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLScqAjH-VU58o38Nt3hB2Bwi-DF0LsR0_r9kwZvjESX52av43Q/viewform?usp=sf_link")  

    time.sleep(2)

    
    address = driver.find_element(By.XPATH, address_xpath)
    price = driver.find_element(By.XPATH, price_xpath)
    link = driver.find_element(By.XPATH, link_xpath)
    submit_button = driver.find_element(By.XPATH, submit_button_xpath)

    
    address.send_keys(all_addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_links[n])
    submit_button.click()


driver.quit()
