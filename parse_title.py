import urllib.request  as urllib2 
from bs4 import BeautifulSoup
from utils import *

def parse_title(soup, id):
    try:
        title = soup.find('title').text
        cleanTitle = remove_tags(title)
        titleStr = cleanTitle[0:-14]
        if titleStr == '':
            return None
    
        return titleStr
    except:
        print('Couldnt parse title for id ' + id)
        return None