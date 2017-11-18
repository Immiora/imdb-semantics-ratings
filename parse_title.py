import urllib.request  as urllib2 
from bs4 import BeautifulSoup
from utils import *

def parse_title(xmlFile):
    title = xmlFile.find('title').text
    cleanTitle = remove_tags(title)
    titleStr = cleanTitle[0:-14]
    if titleStr == '':
        return None
    
    return titleStr