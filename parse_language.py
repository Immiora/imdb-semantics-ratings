import urllib.request  as urllib2 
from bs4 import BeautifulSoup
from utils import *

def parse_language(xmlFile):
    for h4 in xmlFile.find_all('h4'):
        if "Language:" in h4:
            language = h4.findNext().text 

    return language
    
