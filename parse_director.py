import urllib.request  as urllib2 
from bs4 import BeautifulSoup
from utils import *

def parse_director(htmlFile):
    directorLines = htmlFile.find_all('span', {'class': 'itemprop'})
    for l in directorLines:
        print(l)