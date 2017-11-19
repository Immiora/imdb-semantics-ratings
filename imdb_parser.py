import urllib.request as urllib2
from bs4 import BeautifulSoup
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
import pandas as pd
 
raw_ids = readIdsFromKaggle()
ids = []
titles = []
casts = []
directors = []
writers = []
popularities = []
countries = []
grosses = []
languages = []
releaseDates = []
ratings = []
locations = []
companies = []


i = 0
for id in raw_ids:
    print(i)
    i = i + 1
    url = id_to_main_page_url(id)
    print(url)
    page = urllib2.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')

    ids.append(id)
    titles.append(parse_title(soup, id))
    casts.append(parse_cast(soup, id))
    directors.append(parse_director(soup, id))
    writers.append(parse_writers(soup, id))
    popularities.append(parse_popularity(soup, id))
    countries.append(parse_country(soup, id))
    grosses.append(parse_gross(soup, id))
    languages.append(parse_language(soup, id))
    ratings.append(get_rating(soup, id))
    locations.append(get_location(soup, id))
    companies.append(parse_company(soup, id))
    if i == 1:
        break

dataFrame = pd.DataFrame({'id': ids, 'titles': titles,\
 'casts': casts, 'directors': directors, 'writers': writers,\
  'popularities': popularities, 'countries': countries, 'grosses': grosses,\
  'languages':languages, 'ratings':ratings, 'locations': locations,\
  'companies': companies})
dataFrame.to_csv('attributes.csv', sep=';')

