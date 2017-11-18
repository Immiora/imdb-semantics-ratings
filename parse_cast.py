import urllib.request  as urllib2 
from bs4 import BeautifulSoup
from utils import *

def parse_cast(xmlFile, id):
    try:
        actorLines = xmlFile.find('div', {'class':'article', 'id':'titleCast'}).find_all('img')
        if (len(actorLines) >= 3):
            return [actorLines[0]['title'], actorLines[1]['title'], actorLines[2]['title']]
    except:
        print('Could parse cast for id ' + id)
        return None
