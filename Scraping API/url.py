import requests
import urllib.parse
import base64

def get_place_details(hint, city):
    url = f"https://www.nobroker.in/api/v1/localities/autocomplete/_search?hint={hint}&city={city}&page=default"
    print(url)
    response = requests.get(url)
    
    try:
        response.raise_for_status()  # Check for HTTP errors
        print(response.text)  # Print response text for debugging
        data = response.json()
        if data and data.get('predictions'):
            return data['predictions'][0]  # Get the first prediction
    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error occurred: {err}")
    except requests.exceptions.JSONDecodeError as err:
        print(f"JSON Decode Error occurred: {err}")
    
    return None


def create_property_url(place_details):
    if place_details is None:
        return None

    city = place_details.get('city')
    locality = place_details.get('structured_formatting', {}).get('main_text')
    search_param = base64.b64encode(locality.encode('utf-8')).decode('utf-8')
    place_id = place_details.get('place_id')

    base_url = "https://www.nobroker.in/property/sale/"
    url = f"{base_url}{city}/{locality}?searchParam={search_param}&radius=2.0&city={city}&locality={locality}&place_id={place_id}"

    return url


# Example usage
hint = "whitefield"
city = "bangalore"

place_details = get_place_details(hint, city)
print(place_details)

url = create_property_url(place_details)
print()
print(url)
