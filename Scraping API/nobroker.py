import requests
from bs4 import BeautifulSoup

url = "https://www.nobroker.in/property/sale/chennai/Chennai%20Apollo?searchParam=W3sibGF0IjoxMi44NjA2MzUyLCJsb24iOjc5Ljk0NDU2ODEsInBsYWNlSWQiOiJDaElKZXpkeDRMN3hVam9SMHVuMXJlRkxBVmMiLCJwbGFjZU5hbWUiOiJDaGVubmFpIEFwb2xsbyIsInNob3dNYXAiOmZhbHNlfV0="

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

listings = soup.find_all("div", class_="bg-white rounded-4 bg-clip-padding overflow-hidden my-1.2p mx-0.5p tp:border-b-0 shadow-defaultCardShadow tp:shadow-cardShadow tp:mt-0.5p tp:mx-0 tp:mb:1p hover:cursor-pointer nb__2_XSE")

for listing in listings:
    title = listing.find("h2", class_="heading-6 flex items-center font-semi-bold m-0").text.strip()
    price = listing.find("div", class_="font-semi-bold heading-6").text.strip()
    location_tag = listing.find("div", class_="mt-0.5p overflow-hidden overflow-ellipsis whitespace-nowrap max-w-70 text-gray-light leading-4 po:mb-0.1p po:max-w-95")
    location = location_tag.text.strip() if location_tag else "Location not found"

    sq_foot_tag = listing.find("div", class_="flex", id="unitCode")
    sq_foot = sq_foot_tag.text.strip() if sq_foot_tag else "Square footage not found"

    details_link = listing.find("a", class_="overflow-hidden overflow-ellipsis whitespace-nowrap max-w-80pe po:max-w-full")
    link = "https://www.nobroker.in" + details_link["href"] if details_link else "Details link not found"

    details_response = requests.get(link)
    details_soup = BeautifulSoup(details_response.content, "html.parser")

    meta_tag = details_soup.find("meta", property="og:image")

    if meta_tag is not None:
        image_url = meta_tag["content"]
    
    print("Title:", title)
    print("Price:", price)
    print("Location:", location)
    print("More details Link:", link)
    print("Square Footage:", sq_foot)
    print("Image Links:", image_url)
    print()
