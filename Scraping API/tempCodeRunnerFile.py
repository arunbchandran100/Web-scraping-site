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


options = Options()
options.headless = True 
driver = webdriver.Chrome(options=options)

city = "bangalore"
locality = "whitefield"
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
