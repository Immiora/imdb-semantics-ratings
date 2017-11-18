import urllib.request  as urllib2 
from bs4 import BeautifulSoup
from utils import *

def parse_popularity(xmlFile, id):
    popularityDownTag = xmlFile.find('span', {'class': 'popularityDown'})
    try:
        popularity = popularityDownTag.findPrevious().findPrevious().text.strip().split()[0]
        return popularity
    except:
        print('Couldnt parse popularity for id ' + id)
        return None