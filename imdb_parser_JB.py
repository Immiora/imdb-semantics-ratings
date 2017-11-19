import urllib.request  as urllib2 
from bs4 import BeautifulSoup
import os
import parsers as prs
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



IDs=readIdsFromKaggle()



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

for i, id in enumerate(IDs[:3000]):
    try:
        print(i)
        soup = get_soup(id)
        D['IDs'].append(id)
        D['titles'].append(prs.parse_title(soup, id))
        D['casts'].append(prs.parse_cast(soup, id))
        D['directors'].append(prs.parse_director(soup, id))
        D['writers'].append(prs.parse_writers(soup, id))
        D['popularities'].append(prs.parse_popularity(soup, id))
        D['deltaPopularities'].append(prs.parse_deltaPopularity(soup, id))
        D['numberReviews'].append(prs.parse_numOfReviews(soup, id))
        D['countries'].append(prs.parse_country(soup, id))
        D['grosses'].append(prs.parse_gross(soup, id))
        D['languages'].append(prs.parse_language(soup, id))
        D['releaseDates'].append(prs.parse_releaseDate(soup, id))
        D['budget'].append(prs.parse_budget(soup, id))
        D['ratings'].append(prs.parse_rating(soup, id))
        D['locations'].append(prs.parse_location(soup, id))
        D['companies'].append(prs.parse_company(soup, id))
        D['storylines'].append(prs.parse_storyline(soup))
        D['keywords'].append(prs.parse_keyword(soup))
        D['genres'].append(prs.parse_genre(soup))
        D['durations'].append(prs.parse_runtime(soup))
        D['colors'].append(prs.parse_color(soup))
        D['aspectRatios'].append(prs.parse_aspect_ratio(soup))
        D['mpaaRatings'].append(prs.parse_mpaa_rating(soup))
    except:
        print("Error with id " + id)
        pass


DF = pd.DataFrame(D) if check_good_dict(D) else None
save_data_frame(DF)

##
# import seaborn as sns
# df = pd.read_csv('kaggle_1000.csv', sep=';')
# sns.distplot(df['ratings'].dropna())
## nan ratings for [310, 335, 416, 519, 534, 545, 610, 643, 719, 747, 772, 949, 966]

##
