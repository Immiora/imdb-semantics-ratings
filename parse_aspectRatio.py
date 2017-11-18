import urllib.request  as urllib2 
from bs4 import BeautifulSoup
from utils import *

def parse_aspectRatio(xmlFile):
    for h4 in xmlFile.find_all('h4'):
        if "Aspect Ratio:" in h4:
            aspectRatio = h4.next_sibling.strip().split()[0]
    return aspectRatio