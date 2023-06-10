import requests
from bs4 import BeautifulSoup

def search_location(state, city):
    base_url = "https://www.nobroker.in"
    
    # Construct the URL for the desired location
    location_url = f"{base_url}/property/sale/{state}/{city}"
    
    # Perform a GET request to the location URL
    response = requests.get(location_url)
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Extract the link or URL of the desired location from the parsed HTML
    link_element = soup.find("a", class_="card-link")  # Replace "card-link" with the correct class containing the link
    if link_element:
        link = base_url + link_element["href"]
        return link
    
    return None

link = search_location('bangalore', 'South%20Avenue')
print("Link:", link)
