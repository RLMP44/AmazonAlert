import requests
import lxml
from bs4 import BeautifulSoup

PRODUCT_URL = "https://www.amazon.com/Microphone-Loop-Out-Recorder-Streaming-Conference/dp/B08SBTK4QH/ref=sr_1_5?crid=V111270S4MTG&keywords=capture+card+ps4+to+laptop&qid=1687403013&sprefix=capture+card+ps4+to+laptop%2Caps%2C255&sr=8-5"
header = {
    "Accept-Language":"en-US,en;q=0.9,ja;q=0.8",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    }

response = requests.get(PRODUCT_URL, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)