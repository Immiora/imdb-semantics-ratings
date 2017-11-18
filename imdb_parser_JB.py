import urllib.request  as urllib2 
from bs4 import BeautifulSoup
import os
from parser_attributes_JB import *
from parse_title import parse_title
from parse_cast import parse_cast
from parse_director import parse_director
from parse_writers import parse_writers
from parse_numOfReviews import parse_numOfReviews
from parse_popularity import parse_popularity
from parse_deltaPopularity import parse_deltaPopularity
from parse_country import parse_country
from parse_gross import parse_gross
from parse_language import parse_language
from parser_rating import get_rating
from parse_location import get_location
from parse_company import parse_company
from parse_releaseDate import parse_releaseDate
from parse_budget import parse_budget

from readIDfromKaggle import *
from readIDfromKaggle import readIdsFromKaggle
import pandas as pd

def get_soup(id):
    quote_page = 'http://www.imdb.com/title/' + id + '/?ref_=nv_sr_2'
    page = urllib2.urlopen(quote_page)
    return BeautifulSoup(page, 'html.parser')

def check_good_dict(D):
    return True if sum([len(i) for _,i in D.items()])/float(len(D.keys()))==len(D['IDs']) else False

def save_data_frame(DF):
    if DF is not None:
        i = 0
        while os.path.exists('kaggle_attr%s.csv' % i):
            i += 1
        DF.to_csv('kaggle_attr%s.csv' % i, sep=';', encoding='utf-8')
        print('Saved to ' + 'kaggle_attr%s.csv' % i)

##

IDs=readIdsFromKaggle()

##

D = {}
D['IDs'] = []
D['titles'] = []
D['casts'] = []
D['directors'] = []
D['writers'] = []
D['popularities'] = []
D['deltaPopularities'] = []
D['numberReviews'] = []
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

for i, id in enumerate(IDs[:10]):
    try:
        print(i)
        soup = get_soup(id)
        D['IDs'].append(id)
        D['titles'].append(parse_title(soup, id))
        D['casts'].append(parse_cast(soup, id))
        D['directors'].append(parse_director(soup, id))
        D['writers'].append(parse_writers(soup, id))
        D['popularities'].append(parse_popularity(soup, id))
        D['deltaPopularities'].append(parse_deltaPopularity(soup, id))
        D['numberReviews'].append(parse_numOfReviews(soup, id))
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
save_data_frame(DF)

##
# import seaborn as sns
# df = pd.read_csv('kaggle_1000.csv', sep=';')
# sns.distplot(df['ratings'].dropna())
## nan ratings for [310, 335, 416, 519, 534, 545, 610, 643, 719, 747, 772, 949, 966]

##
