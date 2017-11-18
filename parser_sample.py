import urllib.request  as urllib2 
from bs4 import BeautifulSoup


def parse_random_attribute(soup):
    title = soup.find('title')
    print(title)
