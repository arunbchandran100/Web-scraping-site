from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response

class SubmitFormAPIView(APIView):
    def post(self, request):
        data = request.data
        city = data.get('city')
        place = data.get('place')
        print(city,place)
        # Return a JSON response
        return Response({'success': True, 'message': 'Form data submitted successfully.'})


def apicall_nobroker(request):

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
        
def apicall_99acres(requests):

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
def apicall_squareyards(requests):
         
        url = "https://www.squareyards.com/sale/property-for-sale-in-hyderabad"

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
