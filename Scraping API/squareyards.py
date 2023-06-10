import requests
from bs4 import BeautifulSoup

url = "https://www.squareyards.com/sale/property-for-sale-in-hyderabad"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

listings = soup.find_all("div", class_="tlBx")

for listing in listings:
    title = listing.find("div", class_="tileProjectName").text.strip()
    price = listing.find("span", class_="tlPrc DSE_Resale_D18").text.strip()
    location = listing.find("span", class_="DSE_Resale_D18").find_all(text=True, recursive=False)[-1].strip()
    sq_foot = listing.find("div", class_="tlSqFt DSE_Resale_D18").text.strip()

    details_button = listing.find("button", onclick=lambda x: x and "helperJS.goToURL" in x)
    link = details_button["onclick"].split("'")[1] if details_button else None

    print("Title:", title)
    print("Price:", price)
    print("Location:", location)
    print("Square Footage:", sq_foot)
    print("More details Link:", link)
    print()
