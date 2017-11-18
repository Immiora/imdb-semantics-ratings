import urllib.request  as urllib2 
from bs4 import BeautifulSoup
from utils import *

def parse_aspectRatio(soup, id):
    try:
        for h4 in soup.find_all('h4'):
            if "Aspect Ratio:" in h4:
                aspectRatio = float(h4.next_sibling.strip().split()[0])
        return aspectRatio
    except:
        print("Couldnt parse aspect ratio (Csilla) for id " + id)