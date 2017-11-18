import urllib.request as urllib2
from bs4 import BeautifulSoup
from parse_title import *


quote_page = 'http://www.imdb.com/title/tt1431045/?ref_=nv_sr_2'
page = urllib2.urlopen(quote_page)
xmlFile = BeautifulSoup(page, 'html.parser')

parse_budget()