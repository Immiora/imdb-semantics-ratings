import numpy as np


def parse_mpaa_rating(xmlFile):
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