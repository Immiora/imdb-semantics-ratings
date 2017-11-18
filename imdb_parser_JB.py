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
from parse_releaseDate import *
from parse_budget import *
from readIDfromKaggle import *
from readIDfromKaggle import readIdsFromKaggle
import pandas as pd

def get_soup(id):
    quote_page = 'http://www.imdb.com/title/' + id + '/?ref_=nv_sr_2'
    page = urllib2.urlopen(quote_page)
    return BeautifulSoup(page, 'html.parser')

def check_good_dict(D):
    return True if sum([len(i) for _,i in D.items()])/float(len(D.keys()))==len(D['ID']) else False

##

IDs=readIdsFromKaggle()

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
D['budget'] = []
D['ratings'] = []
D['locations'] = []
D['companies'] = []
D['storylines'] = []
D['keywords'] = []
D['genres'] = []
D['durations'] = []
D['colors'] = []
D['aspectRatios'] = []
D['mpaaRatings'] = []

for i, id in enumerate(IDs[:1000]):
    try:
        print(i)
        soup = get_soup(id)
        D['ID'].append(id)
        D['titles'].append(parse_title(soup, id))
        D['casts'].append(parse_cast(soup, id))
        D['directors'].append(parse_director(soup, id))
        D['writers'].append(parse_writers(soup, id))
        D['popularities'].append(parse_popularity(get_soup(id), id))
        D['countries'].append(parse_country(soup, id))
        D['grosses'].append(parse_gross(soup, id))
        D['languages'].append(parse_language(soup, id))
        D['releaseDates'].append(parse_releaseDate(soup, id))
        D['budget'].append(parse_budget(soup, id))
        D['ratings'].append(get_rating(soup, id))
        D['locations'].append(get_location(soup, id))
        D['companies'].append(parse_company(soup, id))
        D['storylines'].append(parse_storyline_attribute(soup))
        D['keywords'].append(parse_keyword_attribute(soup))
        D['genres'].append(parse_genre_attribute(soup))
        D['durations'].append(parse_runtime_attribute(soup))
        D['colors'].append(parse_color_attribute(soup))
        D['aspectRatios'].append(parse_aspect_ratio_attribute(soup))
        D['mpaaRatings'].append(parse_mpaa_attribute(soup))
    except:
        print("Error with id " + id)
        pass

##
DF = pd.DataFrame(D) if check_good_dict(D) else None

if DF is not None: DF.to_csv('kaggle_1000.csv', sep=';', encoding='utf-8')

##

# import seaborn as sns
## df = pd.read_csv('kaggle_1000.csv', sep=';')
# sns.distplot(df['ratings'].dropna())
## nan ratings for [310, 335, 416, 519, 534, 545, 610, 643, 719, 747, 772, 949, 966]

##
