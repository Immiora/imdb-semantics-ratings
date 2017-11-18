import urllib.request  as urllib2 
from bs4 import BeautifulSoup
from utils import *

def parse_country(xmlFile):
    for h4 in xmlFile.find_all('h4'):
        if "Country:" in h4:
            country = h4.findNext().text 

    return country