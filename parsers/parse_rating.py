import urllib.request as urllib2
from urllib.request import HTTPError
from bs4 import BeautifulSoup

def parse_rating(soup, id):
    try:
        val = float(soup.find("div", {"class":"ratingValue"}).find("span").text)
        return val
    except:
        print('Couldnt parse rating for id ' + id)
        return None