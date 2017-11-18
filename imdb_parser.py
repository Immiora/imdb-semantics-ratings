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


i = 0
for id in raw_ids:
    print(i)
    i = i + 1
    url = id_to_main_page_url(id)
    page = urllib2.urlopen(url)
    xmlFile = BeautifulSoup(page, 'html.parser')

    ids.append(id)
    titles.append(parse_title(xmlFile, id))
    casts.append(parse_cast(xmlFile, id))
    directors.append(parse_director(xmlFile, id))
    writers.append(parse_writers(xmlFile, id))
    popularities.append(parse_popularity(xmlFile, id))
    countries.append(parse_country(xmlFile, id))
    grosses.append(parse_gross(xmlFile, id))
    languages.append(parse_language(xmlFile, id))
    ratings.append(get_rating(xmlFile, id))
    if i == 20:
        break

dataFrame = pd.DataFrame({'id': ids, 'titles': titles,\
 'casts': casts, 'directors': directors, 'writers': writers,\
  'popularities': popularities, 'countries': countries, 'grosses': grosses,\
  'languages':languages, 'ratings':ratings})
dataFrame.to_csv('attributes.csv', sep=';')

