import urllib.request  as urllib2 
from bs4 import BeautifulSoup
from utils import *

def parse_director(htmlFile):
    directedByLine = htmlFile.find('meta', {'property': 'og:description'})['content']
    return directedByLine[12:].split('.')[0]
    