import numpy as np
from parsers.trim_spaces import trim_spaces


def parse_color(xmlFile):
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