from django.shortcuts import render
from django.http import JsonResponse
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

from rest_framework.views import APIView
from rest_framework.response import Response

class SubmitFormAPIView(APIView):
    def post(self, request):
        data = request.data
        locality = data.get('city')
        place = data.get('place')
        print(locality,place)
        apicall_squareyards(locality,place)
        apicall_99acres(locality,place)
        apicall_nobroker(locality,place)
        # Return a JSON response
        return Response({'success': True, 'message': 'Form data submitted successfully.'})


def apicall_nobroker(city,locality):

    city = 'Pune'
    locality = 'whitefield'

    city = city.lower()
    locality = locality.lower()

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

        
def apicall_99acres(city,locality):

        
    options = Options()
    options.headless = True
    options.add_argument('window-size=1200x800')
    driver = webdriver.Chrome(options=options)

    place = city + " " + locality

    url = "https://www.99acres.com/"
    driver.get(url)
    driver.maximize_window()

    form_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="keyword2"]')))
    form_element.click()
    form_element.send_keys(place)
    form_element.send_keys(Keys.ARROW_DOWN)
    form_element.send_keys(Keys.ENTER)

    time.sleep(5)  
    submit_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="inPageSearchForm"]/div[2]/div/div/div[1]/div[3]/button')))
    submit_btn.click()

    WebDriverWait(driver, 10).until(EC.url_changes(url))

    url_99acres = driver.current_url
    print("Current URL:", url_99acres)

    driver.quit()

    response = requests.get(url_99acres)
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

            
def apicall_squareyards(city,locality):
            
    import requests
    from bs4 import BeautifulSoup



    city1 = city.replace(" ", "-")
    locality1 = locality.replace(" ", "-")

    url = f"https://www.squareyards.com/sale/property-for-sale-in-{locality1.lower()}-{city1.lower()}"

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

        image_container = listing.find("div", class_="tileProjectImgBox thisss smArrow DSE_Resale_D17")
        if image_container:
            image_tags = image_container.find_all("img", class_="img-responsive bx-item lazy DSE_Resale_D17")
            image_links = [img["data-src"] for img in image_tags]

        print("Title:", title)
        print("Price:", price)
        print("Location:", location)
        print("More details Link:", link)
        print("Square Footage:", sq_foot)
        print("Image Links:", image_links)
        print()
