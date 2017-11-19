import numpy as np
from . import trim_spaces

## one-hot encoding over 22 genres
def parse_genre(xmlFile):
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