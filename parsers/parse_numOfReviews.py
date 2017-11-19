import urllib.request as urllib2
from urllib.request import HTTPError
from bs4 import BeautifulSoup

def parse_numOfReviews(soup, id):
    try:
        val1 =int(soup.find("span", {"itemprop":"reviewCount"}).text.split()[0].replace(',',''))
        return val1
    
    except:
        print('Couldnt parse number of reviews for id ' + id)
        return None
