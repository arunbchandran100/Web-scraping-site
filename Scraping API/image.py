import requests
from bs4 import BeautifulSoup

url = "https://www.nobroker.in/property/buy/1-bhk-apartment-for-sale-in-oragadam-industrial-corridor-chennai/8a9fc982826c384101826c9676773c87/detail"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

#<meta property="og:image" content="https://images.nobroker.in/images/8a9fc982826c384101826c9676773c87/8a9fc982826c384101826c9676773c87_53043_95592_large.jpg"/>

meta_tag = soup.find("meta", property="og:image")

if meta_tag is not None:
    image_url = meta_tag["content"]
    print(image_url)
else:
    print("Image URL not found.")


