import os

from bs4 import BeautifulSoup
import lxml
import requests
import smtplib

my_email = os.environ["MYEMAIL"]
my_password = os.environ["MYPASSWORD"]

PRODUCT_URL = "https://www.amazon.com/Microphone-Loop-Out-Recorder-Streaming-Conference/dp/B08SBTK4QH/ref=sr_1_5?crid=V111270S4MTG&keywords=capture+card+ps4+to+laptop&qid=1687403013&sprefix=capture+card+ps4+to+laptop%2Caps%2C255&sr=8-5"
header = {
    "Accept-Language": "en-US,en;q=0.9,ja;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    }

response = requests.get(url=PRODUCT_URL, headers=header)

soup = BeautifulSoup(response.text, "lxml")

price_w = soup.find(class_="a-price-whole").text
price_f = soup.find(class_="a-price-fraction").text
price = float(price_w + price_f)

item = soup.find(id="productTitle").text.strip()
alert = f"The current price for {item} is ${price}.\n Buy it now at: {PRODUCT_URL}"

if price <= 25:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=os.environ["TOADDRS"],
                            msg=f"Subject:Your Item's Price Dropped\n\n{alert}")
