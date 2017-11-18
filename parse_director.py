import urllib.request  as urllib2 
from bs4 import BeautifulSoup
from utils import *

def parse_director(htmlFile, id):
    try:
        directedByLine = htmlFile.find('meta', {'property': 'og:description'})['content']
        return directedByLine[12:].split('.')[0]
    except:
        print('Couldnt parse director for id ' + id)
        return None
    