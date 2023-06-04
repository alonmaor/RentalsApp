# Import Python Libraries

# For HTML parsing
from enum import Enum

from bs4 import BeautifulSoup

# For website connections
import requests

# To prevent overwhelming the server between connections
from time import sleep

# Display the progress bar
from tqdm import tqdm

# For data wrangling
import numpy as np
import pandas as pd

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# For creating plots
import matplotlib.pyplot as plt
import plotly.graph_objects as go


class Areas(Enum):
    TELAVIV=1
    NORTH=5


class Cities(Enum):
    TELAVIV=5000
    HAIFA=4000


def get_page(city=None, type=None, beds=None, page=None):
    print(Areas.TELAVIV)
    url = f'https://gw.yad2.co.il/feed-search-legacy/realestate/rent?topArea=19&area=18&city=6400&propertyGroup=apartments&property=1&rooms=3-4&price=4000-4500&forceLdLoad=true'
    print(url)

    result = requests.get(url)
    print(result.content)

    # check HTTP response status codes to find if HTTP request has been successfully completed
    if result.status_code >= 100 and result.status_code <= 199:
        print('Informational response')
    if result.status_code >= 200 and result.status_code <= 299:
        print('Successful response')
        soup = BeautifulSoup(result.content, "json5")
    if result.status_code >= 300 and result.status_code <= 399:
        print('Redirect')
    if result.status_code >= 400 and result.status_code <= 499:
        print('Client error')
    if result.status_code >= 500 and result.status_code <= 599:
        print('Server error')

    return soup


# for page_num in tqdm(range(1, 250)):
#     sleep(2)
#
#     # get soup object of the page
#     soup_page = get_page('toronto', 'condos', '1', page_num)
#
#     # grab listing street
#     for tag in soup_page.find_all('div', class_='listing-brief'):
#         for tag2 in tag.find_all('span', class_='replace street'):
#             # to check if data point is missing
#             if not tag2.get_text(strip=True):
#                 listingStreet.append("empty")
#             else:
#                 listingStreet.append(tag2.get_text(strip=True))