from bs4 import BeautifulSoup
import requests
import smtplib
from decouple import config



user_email = config("GMAIL_USERNAME")
user_password = config("GMAIL_PASSWORD")


url = "https://www.amazon.in/dp/B0BGS67H69/ref=sspa_dk_detail_1?psc=1&pd_rd_i=B0BGS67H69&pd_rd_w=SV2Dq&content-id=amzn1.sym.2575ab02-73ff-40ca-8d3a-4fbe87c5a28d&pf_rd_p=2575ab02-73ff-40ca-8d3a-4fbe87c5a28d&pf_rd_r=73BVD4E2ZWXVYJEC2RKB&pd_rd_wg=ijjpQ&pd_rd_r=93aee7b8-3f71-4ec7-a586-f9841f956e1d&s=shoes&sp_csd=d2lkZ2V0TmFtZT1zcF9kZXRhaWw"

header ={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Accept-Language" : "en-US,en;q=0.9"
}

response = requests.get(url , headers=header)
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.text)
price = soup.find( class_="a-price-whole").getText()

price_replace = price.replace(",","")
int_price = int(price_replace)


title = soup.find(id="productTitle").get_text().strip()
print(title)

BUY_PRICE = 1000

if int_price < BUY_PRICE:
    message = f"{title} is now {price}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=user_email , password=user_password)
        connection.sendmail(from_addr= user_email , 
                            to_addrs=user_email,
                            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
                            )