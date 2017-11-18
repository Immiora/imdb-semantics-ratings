import urllib.request as urllib2
from urllib.request import HTTPError
from bs4 import BeautifulSoup

def parse_deltaPopularity(soup, id):
    try:
        val1 =float(soup.find("span", {"class":"popularityUpOrFlat"}).text.split()[0].replace(',','.'))
        return val1
    
    except:
        print('Couldnt parse delta popularity for id ' + id)
        return None
