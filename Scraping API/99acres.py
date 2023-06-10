import requests
from bs4 import BeautifulSoup

url = "https://www.99acres.com/search/property/buy/hyderabad?city=269&preference=S&area_unit=1&res_com=R"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

listings = soup.find_all("a", class_="projectTuple__projectName")
for listing in listings:
    title = listing.text.strip()

    print("Title:", title)
    print()
