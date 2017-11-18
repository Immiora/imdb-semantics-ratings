import urllib.request  as urllib2 
from bs4 import BeautifulSoup
from utils import *

def parse_releaseDate(soup):
    for h4 in soup.find_all('h4'):
        if "Release Date:" in h4:
            releaseDate = h4.next_sibling.strip()      
    return releaseDate
