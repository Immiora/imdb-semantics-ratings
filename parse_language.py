import urllib.request  as urllib2 
from bs4 import BeautifulSoup
from utils import *

def parse_language(xmlFile, id):
    try:
        for h4 in xmlFile.find_all('h4'):
            if "Language:" in h4:
                language = h4.findNext().text 

        return language
    except:
        print('Couldnt parse language for id ' + id)
        return None
