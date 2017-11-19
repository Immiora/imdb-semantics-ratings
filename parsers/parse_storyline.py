from parsers.trim_spaces import trim_spaces

def parse_storyline(xmlFile):
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