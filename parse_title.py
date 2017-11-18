import urllib.request  as urllib2 
from bs4 import BeautifulSoup
from utils import *

def parse_title(xmlFile):
    title = xmlFile.find('title').text
    cleanTitle = remove_tags(title)
    return cleanTitle.split()[0]