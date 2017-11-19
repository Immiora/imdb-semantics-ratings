import urllib.request  as urllib2 
from bs4 import BeautifulSoup
from utils import *

def parse_language(soup, id):
    try:
        for h4 in soup.find_all('h4'):
            if "Language:" in h4:
                language = h4.findNext().text 
                return language
        return None
        
    except:
        print('Couldnt parse language for id ' + id)
        return None
