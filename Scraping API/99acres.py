import requests
from bs4 import BeautifulSoup

url = "https://www.99acres.com/search/property/buy/hyderabad?city=269&preference=S&area_unit=1&res_com=R"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
listings = soup.find_all("div", class_="projectTuple__descCont")

for listing in listings:
    project_name_element = listing.find("a", class_="projectTuple__projectName")
    project_name = project_name_element.get_text(strip=True)

    price_element = listing.find("span", class_="configurationCards__srpPriceHeading")
    price = price_element.get_text(strip=True)

    location_element = listing.find("h2", class_="projectTuple__subHeadingWrap body_med ellipsis")
    location = location_element.get_text(strip=True)

    link_element = listing.find("a", class_="projectTuple__projectName")
    link = link_element["href"]

    """usp_description_element = listing.find('span', class_='caption_subdued_medium configurationCards__cardAreaSubHeadingOne')
    if usp_description_element:
        usp_description = usp_description_element.get_text(strip=True)
        sq_foot = usp_description.split()[0]  # Extract the first word, which represents the square footage
    else:
        sq_foot = "N/A" """

    details_response = requests.get(link)
    details_soup = BeautifulSoup(details_response.content, "html.parser")

    usp_description_element = details_soup.find('span', class_='caption_subdued_medium configurationCards__cardAreaSubHeadingOne')
    if usp_description_element:
        sq_foot_range = usp_description_element.get_text(strip=True)
    else:
        sq_foot_range = "N/A"


    image_elements = details_soup.find_all('div', class_='PhotonCard__photonDisp')
    image_urls = [img.find('img')['src'] for img in image_elements]

    print("Title:", project_name)
    print("Price:", price)
    print("Location:", location)
    print("More details Link:", link)
    print("Square Footage:", sq_foot_range)
    print("Image Links:", image_urls)
    print()
