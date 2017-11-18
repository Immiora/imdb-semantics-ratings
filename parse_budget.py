import urllib.request  as urllib2 
from bs4 import BeautifulSoup
from utils import *

def parse_budget(xmlFile):
    for h4 in xmlFile.find_all('h4'):
        if "Budget:" in h4:
            budget = h4.next_sibling.strip()
    return budget
