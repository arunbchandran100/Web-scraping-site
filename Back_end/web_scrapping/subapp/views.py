from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.http import JsonResponse
        
# from .models import Homepage

def Homepage(request):
    if request.method =='POST':
        city = request.POST['city']
        place = request.POST['place']
        
        print(city)
        print(place)
    return render(request, 'register/location.html',{})

def index(request):
    return render(request,'index.html')


def apicall_nobroker(request):
    url = "https://www.nobroker.in/property/sale/chennai/Chennai%20Apollo?searchParam=W3sibGF0IjoxMi44NjA2MzUyLCJsb24iOjc5Ljk0NDU2ODEsInBsYWNlSWQiOiJDaElKZXpkeDRMN3hVam9SMHVuMXJlRkxBVmMiLCJwbGFjZU5hbWUiOiJDaGVubmFpIEFwb2xsbyIsInNob3dNYXAiOmZhbHNlfV0="
    response = requests.get(url)
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
            "title": title,
            "price": price,
            "location": location,
            "link": link,
            "square_footage": sq_foot,
            "image_url": image_url
        }
        results.append(result)

    return JsonResponse(results, safe=False)

        


def apicall_99acres(request):
    import requests
    from bs4 import BeautifulSoup

    url = "https://www.99acres.com/search/property/buy/hyderabad?city=269&preference=S&area_unit=1&res_com=R"

    response = requests.get(url)
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
            "Title": project_name,
            "Price": price,
            "Location": location,
            "More details Link": link,
            "Square Footage": sq_foot_range,
            "Image Links": image_urls
        }

        data.append(listing_data)

    return JsonResponse(data, safe=False)


        


def apicall_squareyards(request):
    url = "https://www.squareyards.com/sale/property-for-sale-in-hyderabad"

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
            "Title": title,
            "Price": price,
            "Location": location,
            "More details Link": link,
            "Square Footage": sq_foot,
            "Image Links": image_links
        }

        scraped_data.append(scraped_item)

    return JsonResponse(scraped_data, safe=False)
