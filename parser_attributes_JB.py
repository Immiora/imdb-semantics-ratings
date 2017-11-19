import urllib.request  as urllib2 
from bs4 import BeautifulSoup
import numpy as np
import trim_spaces




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

