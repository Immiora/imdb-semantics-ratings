import urllib.request  as urllib2 
from bs4 import BeautifulSoup
from utils import *

def parse_company(xmlFile):
    for h3 in xmlFile.find_all('h3'):
        if "Company Credits" in h3:
            company = h3.findNext().text.strip().split('\n')[2]

    return company
    