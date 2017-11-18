import urllib.request  as urllib2 
from bs4 import BeautifulSoup
from utils import *

def parse_popularity(soup, id):
    
    try:
        popularityDownTag = soup.find('span', {'class': 'popularityDown'})
        popularity = popularityDownTag.findPrevious().findPrevious().text.strip().split()[0]
        return popularity

    except:
        a=5

    try:
        popularityDownTag = soup.find('span', {'class': 'popularityUpOrFlat'})
        popularity = popularityDownTag.findPrevious().findPrevious().text.strip().split()[0]
        return popularity
    except:
        print('Couldnt parse popularity for id ' + id)
        return None