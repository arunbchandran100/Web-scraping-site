from django.shortcuts import render
from django.http import JsonResponse
from .models import Listing
import requests# Add this line
from bs4 import BeautifulSoup
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Listing
import time
import logging
import requests
from bs4 import BeautifulSoup
import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from .models import Listing

from rest_framework.views import APIView
from rest_framework.response import Response

import time

locality = None
city = None

class SubmitFormAPIView(APIView):

    def post(self, request):
        global locality,city
        data = request.data
        city = data.get('city')
        locality= data.get('place')
        city = city.lower()
        locality = locality.lower()
        print(locality, city)

        # Call the functions sequentially with delays
        #square_data = apicall_squareyards(self,city=place,locality=locality)
        #print(square_data)
        # data=apicall_99acres(locality, place)
        #apicall_nobroker(locality, place)

        # Return a JSON response
        return JsonResponse({'success': True })#'data': square_data})
    
"""class FetchData(APIView):

    def get(self, request):
        
        print(locality, place)

        #square_data = apicall_squareyards(self)
        #print(square_data)
        # data=apicall_99acres(locality, place)
        #apicall_nobroker(locality, place)

        # Return a JSON response
        return Response({'data': square_data})
    """


def aggregate_api_calls(request):
    squareyards_data = apicall_squareyards(request)
    acres99_data = apicall_99acres(request)
    #nobroker_data = apicall_nobroker(request)
    
    # Combine all data into one list
    combined_data = squareyards_data + acres99_data# + nobroker_data

    return JsonResponse(combined_data, safe=False)


def product_data(request):
    
    title = "Some title"
    price = 100
    location = "Some location"
    link = "https://example.com/details"
    sq_foot = "200 sq feet"
    image_url = "https://mediacdn.99acres.com/media1/20490/18/409818766M-1677649238457.jpg"

    product_item = []
    product_data ={
            "id": 1,
            "title": title,
            "price": price,
            "location": location,
            "more_details_link": link,
            "square_footage": sq_foot,
            "image_urls": image_url,
        }
        # Add more product data as needed
                
                
    product_item.append(product_data)


    return JsonResponse(product_item, safe=False)


def get_data(request):
    data = Listing.objects.all()

    # Convert the data to JSON format
    json_data = [
        {
            'city': item.city,
            'locality': item.locality
        }
        for item in data
    ]

    return JsonResponse(json_data, safe=False)


def apicall_nobroker(request):


    options = Options()
    options.headless = True
    options.add_argument('window-size=1200x800')
    driver = webdriver.Chrome(options=options)
    options.add_argument("--disable-notifications") 
    driver = webdriver.Chrome(options=options)

    url = "https://www.nobroker.in/"
    driver.get(url)
    driver.maximize_window()

    rent_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[1]/div[3]/div[1]')))
    rent_button.click()

    dropdown_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "nb-select__control")))
    dropdown_button.click()

    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "nb-select__menu-list")))

    cities = ['mumbai', 'bangalore', 'pune', 'chennai', 'gurgaon', 'hyderabad', 'delhi', 'noida', 'greater noida', 'ghaziabad', 'faridabad']
    index = cities.index(city)

    dropdown_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "react-select-2-input")))
    time.sleep(3) 
    dropdown_input.send_keys(Keys.ARROW_UP)

    for _ in range(index):
        dropdown_input.send_keys(Keys.ARROW_DOWN)
        time.sleep(0.5) 

    dropdown_input.send_keys(Keys.ENTER)


    form_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="listPageSearchLocality"]')))
    form_element.click()
    form_element.send_keys(locality)

    time.sleep(2)
    form_element.send_keys(Keys.ARROW_DOWN)
    form_element.send_keys(Keys.ENTER)

    time.sleep(2)  
    submit_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[1]/div[4]/button')))
    submit_btn.click()

    WebDriverWait(driver, 10).until(EC.url_changes(url))

    url_nobroker = driver.current_url

    driver.quit()

    response = requests.get(url_nobroker)
    soup = BeautifulSoup(response.content, "html.parser")

    listings = soup.find_all("div", class_="bg-white rounded-4 bg-clip-padding overflow-hidden my-1.2p mx-0.5p tp:border-b-0 shadow-defaultCardShadow tp:shadow-cardShadow tp:mt-0.5p tp:mx-0 tp:mb:1p hover:cursor-pointer nb__2_XSE")

    results = []
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
        image_url = meta_tag["content"] if meta_tag else ""

        result = {
            "id": 1,
            "title": title,
            "price": price,
            "location": location,
            "more_details_link": link,
            "square_footage": sq_foot,
            "image_urls": image_url
        }
        results.append(result)

    #return JsonResponse(results, safe=False)
    return results

            
import requests
from bs4 import BeautifulSoup
import json

def apicall_squareyards(request):

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

        scraped_item = {
            "id": 1,
            "title": title,
            "price": price,
            "location": location,
            "more_details_link": link,
            "square_footage": sq_foot,
            "image_urls": image_links
        }

        scraped_data.append(scraped_item)
        
        #print(scraped_data)  # Print scraped data for debugging

    try:
        return scraped_data
        #return JsonResponse(scraped_data, safe=False)
    except Exception as e:
        print(e)  # Print the exception for debugging
        raise e
    #return JsonResponse(json_data, safe=False)
    
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import requests
from bs4 import BeautifulSoup

#@method_decorator(csrf_exempt, name='dispatch')
#class ApiCall99acresView(View):
def apicall_99acres(request):

        place = locality + " " + city
        preference = "S"
        rescom = "R"
        format_type = "APP"
        search_type = "COWORKING"
        page_name = "homePage"
        platform = "DESKTOP"

        url = f"https://s.99acres.com/api/autocomplete/suggest?term={place}&PREFERENCE={preference}&RESCOM={rescom}&FORMAT={format_type}&SEARCH_TYPE={search_type}&CITY=&landmarkRequired=true&pageName={page_name}&platform={platform}"

        response = requests.get(url)
        data = response.json()

        # Extract data from the first suggestion
        first_suggestion = data['suggest'][0]
        name = first_suggestion['NAME']
        property_count = first_suggestion['PROPERTY_COUNT']
        marker = first_suggestion['MARKER']
        city1 = first_suggestion['CITY']
        preference = first_suggestion['PREFERENCE']
        rescom = first_suggestion['RESCOM']
        e_type = first_suggestion['E_TYPE']

        # Replace spaces with hyphens in the place name
        name = name.replace(" ", "-")

        # Constructing the URL
        base_url = "https://www.99acres.com/search/property/buy/"

        if e_type == "City":
            url_99acres = f"{base_url}{name.lower()}?city={city1}&preference={preference}&area_unit=1&res_com={rescom}"
        else:
            locality_id = marker.split("_LOCALITY_")[-1]
            url_99acres = f"{base_url}{name.lower()}?city={city1}&locality={locality_id}&preference={preference}&area_unit=1&res_com={rescom}"

        print("Constructed URL for 99acres:", url_99acres)

        response = requests.get(url_99acres)
        soup = BeautifulSoup(response.content, "html.parser")
        listings = soup.find_all("div", class_="projectTuple__descCont")

        data = []

        for listing in listings:
            project_name_element = listing.find("a", class_="projectTuple__projectName")
            project_name = project_name_element.get_text(strip=True)

            price_element = listing.find("span", class_="configurationCards__srpPriceHeading")
            price = price_element.get_text(strip=True)

            location_element = listing.find("h2", class_="projectTuple__subHeadingWrap body_med ellipsis")
            location = location_element.get_text(strip=True)

            link_element = listing.find("a", class_="projectTuple__projectName")
            link = link_element["href"]

            details_response = requests.get(link)
            details_soup = BeautifulSoup(details_response.content, "html.parser")

            usp_description_element = details_soup.find('span', class_='caption_subdued_medium configurationCards__cardAreaSubHeadingOne')
            if usp_description_element:
                sq_foot_range = usp_description_element.get_text(strip=True)
            else:
                sq_foot_range = "N/A"

            image_elements = details_soup.find_all('div', class_='PhotonCard__photonDisp')
            image_urls = [img.find('img')['src'] for img in image_elements]

            listing_data = {
                "id": 1,
                "title": project_name,
                "price": price,
                "location": location,
                "more_details_link": link,
                "square_footage": sq_foot_range,
                "image_urls": image_urls
            }

            data.append(listing_data)

        return data



