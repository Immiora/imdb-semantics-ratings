from parsers.trim_spaces import trim_spaces

def parse_keyword(xmlFile):
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