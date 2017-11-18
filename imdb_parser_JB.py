import urllib.request  as urllib2 
from bs4 import BeautifulSoup
from parser_attributes_JB import *
from parse_title import *
from parse_cast import *
from parse_director import *
from parse_writers import *
from parse_popularity import *
from parse_country import *
from parse_gross import *
from parse_language import *
from parser_rating import *
from parse_location import *
from parse_company import *
from readIDfromKaggle import *
from readIDfromKaggle import readIdsFromKaggle
import pandas as pd

def get_soup(id):
    quote_page = 'http://www.imdb.com/title/' + id + '/?ref_=nv_sr_2'
    page = urllib2.urlopen(quote_page)
    return BeautifulSoup(page, 'html.parser')


##
# with open("test.html", "w", encoding="utf-8") as file:
#     file.write(str(xmlFile))


##
D = {}
D['ID'] = []
D['titles'] = []
D['casts'] = []
D['directors'] = []
D['writers'] = []
D['popularities'] = []
D['countries'] = []
D['grosses'] = []
D['languages'] = []
D['releaseDates'] = []
D['ratings'] = []
D['locations'] = []
D['companies'] = []
D['storylines'] = []
D['keywords'] = []

##
IDs=readIdsFromKaggle()
for id in IDs[:10]:
    soup = get_soup(id)
    D['ID'].append(id)
    D['titles'].append(parse_title(soup, id))
    D['casts'].append(parse_cast(soup, id))
    D['directors'].append(parse_director(soup, id))
    D['writers'].append(parse_writers(soup, id))
    D['popularities'].append(parse_popularity(soup, id))
    D['countries'].append(parse_country(soup, id))
    D['grosses'].append(parse_gross(soup, id))
    D['languages'].append(parse_language(soup, id))
    D['ratings'].append(get_rating(soup, id))
    D['locations'].append(get_location(soup, id))
    D['companies'].append(parse_company(soup, id))
    D['storylines'].append(parse_storyline_attribute(soup))
    D['keywords'].append(parse_keyword_attribute(soup))

##
pd.DataFrame(D)


