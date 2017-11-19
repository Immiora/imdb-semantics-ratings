import urllib.request  as urllib2 
from bs4 import BeautifulSoup
from utils import *

def parse_company(soup, id):
    try:
        for h3 in soup.find_all('h3'):
            if "Company Credits" in h3:
                company = h3.findNext().text.strip().split('\n')[2]
                return company
        return None
        
    except:
        print('Couldnt parse company for id ' + id)
        return None
    