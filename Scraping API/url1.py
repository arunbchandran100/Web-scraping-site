from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

city = 'Bangalore'
locality = 'whitefield'

# Convert both to lowercase
city = city.lower()
locality = locality.lower()

options = Options()
options.add_argument("--disable-notifications")  # Disable notifications
driver = webdriver.Chrome(options=options)

url = "https://www.nobroker.in/"
driver.get(url)
driver.maximize_window()

#for selecting rent
rent_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div/div[1]/div[3]/div[1]')))
rent_button.click()

# Click the dropdown button
dropdown_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "nb-select__control")))
dropdown_button.click()

# Wait for the dropdown options to be loaded
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "nb-select__menu-list")))

# Define the cities in the dropdown
cities = ['mumbai', 'bangalore', 'pune', 'chennai', 'gurgaon', 'hyderabad', 'delhi', 'noida', 'greater noida', 'ghaziabad', 'faridabad']
# Find the index of the desired city
index = cities.index(city)

# Send the city name directly to the input inside the dropdown
dropdown_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "react-select-2-input")))
time.sleep(3) 
dropdown_input.send_keys(Keys.ARROW_UP)

# Send 'down arrow' key events until reaching the desired option
for _ in range(index+1):
    dropdown_input.send_keys(Keys.ARROW_DOWN)
    time.sleep(0.5)  # adding a delay to ensure each key press is registered

# Press ENTER to select the desired city
dropdown_input.send_keys(Keys.ENTER)


#locality
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
print("Current URL:", url_nobroker)

driver.quit()