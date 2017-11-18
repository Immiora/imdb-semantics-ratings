import urllib.request  as urllib2 
from bs4 import BeautifulSoup
import numpy as np

def trim_spaces(str):
    while (str[0]==' ') | (str[-1]==' '):
        if str[0]==' ': str = str[1:]
        if str[-1]==' ': str = str[:-1]
    return str


def parse_storyline_attribute(xmlFile):
    '''
    Returns movie storyline
    :param xmlFile: soup
    :return: string
    '''
    try:
        attrs = {'class': 'inline canwrap', 'itemprop': 'description'}
        out = xmlFile.find('div', attrs).text.replace('\n', '')
        return trim_spaces(out[:out.find('Written')]) if out != '' else None
    except:
        print('Warning: attribute is None')
        return None

def parse_keyword_attribute(xmlFile):
    '''
    Returns movie keywords
    :param xmlFile: soup
    :return: list of strings
    '''
    try:
        attrs = {'class': 'see-more inline canwrap', 'itemprop': 'keywords'}
        return [trim_spaces(i.get_text()) for i in xmlFile.find('div', attrs).find_all('a')][:-1]
    except:
        print('Warning: attribute is None')
        return None


## one-hot encoding over 22 genres
def parse_genre_attribute(xmlFile):
    '''
    Returns genres as one-hot encoding over 22 genres
    :param xmlFile: soup
    :return: array (n_tagged_genres, 22)
    '''
    try:
        genres = ['Action', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime', 'Documentary', 'Drama',
                  'Family', 'Fantasy', 'Film-Noir', 'History', 'Horror', 'Music', 'Musical', 'Mystery',
                  'Romance', 'Sci-Fi', 'Sport', 'Thriller', 'War', 'Western']
        attrs = {'class': 'see-more inline canwrap', 'itemprop': 'genre'}
        scraped = [trim_spaces(i.get_text()) for i in xmlFile.find('div', attrs).find_all('a')]
        out = np.zeros((len(genres),), dtype=np.int16)
        for si in scraped: out[genres.index(si)] = 1
        return out if np.any(out) else None
    except:
        print('Warning: attribute is None')
        return None


## in minutes
def parse_runtime_attribute(xmlFile):
    '''
    Returns movie duration in minutes. If there are more durations, the first one is returned
    :param xmlFile: soup
    :return: int
    '''
    try:
        attrs = {'itemprop': 'duration'}
        return int(xmlFile.find('time', attrs)['datetime'][2:-1])
    except:
        print('Warning: attribute is None')
        return None


def parse_color_attribute(xmlFile):
    '''
    Returns color attribute
    :param xmlFile: soup
    :return: array (2,) where array[0] is color and array[1] is black and white
    '''
    try:
        colors = ['Color', 'Black and White']
        attrs = {'class': 'article', 'id': 'titleDetails'}
        out1= [i['href'] for i in xmlFile.find('div', attrs).find_all('a')]
        out2= [i.text for i in xmlFile.find('div', attrs).find_all('a')]
        idx = [i for i, x in enumerate(['/search/title?colors=' in i for i in out1])if x == True]
        out = np.zeros((len(colors,)), dtype=np.int16)
        for i, si in enumerate(idx): out[colors.index(trim_spaces(out2[si]))] = 1
        return out if np.any(out) else None
    except:
        print('Warning: attribute is None')
        return None


def parse_aspect_ratio_attribute(xmlFile):
    '''
    Returns aspect ratio as a tuple of two dims
    :param xmlFile: soup
    :return: tuple, e.g. (1.34, 1.)
    '''
    try:
        attrs = {'class': 'article', 'id': 'titleDetails'}
        out = trim_spaces(xmlFile.find('div', attrs).find_all('div')[-1].text).replace('\n', '').replace('Aspect Ratio: ', '')
        return float(trim_spaces(out[:out.find(':')])), float(trim_spaces(out[out.find(':')+1:])) if out != '' else None
    except:
        print('Warning: attribute is None')
        return None


def parse_mpaa_attribute(xmlFile):
    '''
    Returns MPAA rating as one-hot encoding over ['G', 'PG', 'PG-13', 'R', 'NC-17']
    :param xmlFile: soup
    :return: array (5,)
    '''
    try:
        mpaa = ['G', 'PG', 'PG-13', 'R', 'NC-17']
        attrs = {'itemprop': 'contentRating'}
        out = xmlFile.find('span', attrs).text
        idx = np.array([' ' + i + ' ' in out for i in mpaa], dtype=bool) * 1
        return idx if np.any(idx) else None
    except:
        print('Warning: attribute is None')
        return None

