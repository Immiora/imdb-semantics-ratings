import urllib.request  as urllib2 
import re
from bs4 import BeautifulSoup
from utils import *

def parse_releaseDate(soup, id):
    try:
        for h4 in soup.find_all('h4'):
            if "Release Date:" in h4:
                releaseDate = h4.next_sibling.strip()
                releaseDate = re.sub("[\(\[].*?[\)\]]", "", releaseDate)
                return releaseDate

        return None

    except:
        print('Could parse release date for id ' + id)
        return None

