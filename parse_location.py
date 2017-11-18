import urllib.request as urllib2
import numpy as np
from urllib.request import HTTPError
from bs4 import BeautifulSoup


def get_location(soup,id):
    try:
        a = soup.find("div",{"class": "article","id": "titleDetails"}).find_all("a")
        hrefs = [i['href'] for i in a]
        idx = [i for i, x in enumerate(['/search/title?locations=' in i for i in hrefs]) if x == True][0]
        return a[idx].text
    except:
        print("couldn't parse location for id " + id)
        return None