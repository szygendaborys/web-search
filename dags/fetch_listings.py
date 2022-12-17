from typing import List
import requests
from bs4 import BeautifulSoup
from listing import Listing

# we want to avoid overquerying and infinite loops
max_page_size = 10


def fetch_listings() -> List[Listing]:
    result = []
    page = 1
    has_more_records = True

    while has_more_records == True and page < max_page_size:
        new_listings = get_listings(page)

        if len(new_listings) == 0:
            has_more_records = False

        result.extend(new_listings)

        page = page + 1

    print(f"Found {len(result)} listings")

    return result


def get_listings(page: int):
    listings = []
    url = f"https://www.otodom.pl/pl/oferty/sprzedaz/dzialka/poznan/szczepankowo?distanceRadius=5&page={page}&limit=36&market=ALL&ownerTypeSingleSelect=ALL&locations=%5Bdistricts_6-2495%5D&priceMax=300000&plotType=%5BBUILDING%5D&by=DEFAULT&direction=DESC&viewType=listing&lang=pl&searchingCriteria=sprzedaz&searchingCriteria=dzialka&searchingCriteria=cala-polska"

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # deprecated
    # response_parent = soup.find(
    #     'div', attrs={"data-cy": "search.listing"}).select('ul > li > a > article')

    elements = []
    response_parent = soup.find_all(
        'a', attrs={"data-cy": "listing-item-link"})

    for parent in response_parent:
        items = parent.select('a > article')
        elements.extend(items)

    for element in elements:
        title = element.select_one('div:nth-of-type(1) > h3')
        meta = element.select_one('div:nth-of-type(2)')
        link = element.parent

        [price, price_per_square, size] = meta.select('span')

        dict = {
            'title': title.text,
            'price': price.text,
            'price_per_square': price_per_square.text,
            'size': size.text,
            'href': link.attrs.get('href')
        }

        listing = Listing(dict)
        listings.append(listing)

    return listings
