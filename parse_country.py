import urllib.request  as urllib2 
from bs4 import BeautifulSoup
from utils import *

def parse_country(soup, id):
    try:
        for h4 in soup.find_all('h4'):
            if "Country:" in h4:
                country = h4.findNext().text 

        return country
    except:
        print('Couldnt parse country for id ' + id)
        return None