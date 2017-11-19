from parsers.trim_spaces import trim_spaces

def parse_aspect_ratio(xmlFile):
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