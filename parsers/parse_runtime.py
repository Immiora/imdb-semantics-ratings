## in minutes
def parse_runtime(xmlFile):
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