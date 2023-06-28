import requests
from bs4 import BeautifulSoup

city = "pune"
locality = "wakad"

city1 = city.replace(" ", "-")
locality1 = locality.replace(" ", "-")

url = f"https://www.squareyards.com/sale/property-for-sale-in-{locality1.lower()}-{city1.lower()}"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

listings = soup.find_all("div", class_="tlBx")

scraped_data = []

for listing in listings:
    title = listing.find("div", class_="tileProjectName").text.strip()
    price = listing.find("span", class_="tlPrc DSE_Resale_D18").text.strip()
    location = listing.find("span", class_="DSE_Resale_D18").find_all(text=True, recursive=False)[-1].strip()
    sq_foot = listing.find("div", class_="tlSqFt DSE_Resale_D18").text.strip()

    details_button = listing.find("button", onclick=lambda x: x and "helperJS.goToURL" in x)
    link = details_button["onclick"].split("'")[1] if details_button else None

    image_container = listing.find("div", class_="tileProjectImgBox thisss smArrow DSE_Resale_D17")
    if image_container:
        image_tags = image_container.find_all("img", class_="img-responsive bx-item lazy DSE_Resale_D17")
        image_links = [img["data-src"] for img in image_tags]

    # Print the details
    print("ID:", len(scraped_data) + 1)
    print("Title:", title)
    print("Price:", price)
    print("Location:", location)
    print("More Details Link:", link)
    print("Square Footage:", sq_foot)
    print("Image URLs:", image_links)
    print()
