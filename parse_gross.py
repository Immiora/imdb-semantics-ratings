import urllib.request  as urllib2 
from bs4 import BeautifulSoup
from utils import *

def parse_gross(soup, id):
    try:
        for h4 in soup.find_all('h4'):
            if "Gross:" in h4:
                grossStr = h4.next_sibling.strip()
                if grossStr[0] == '$':
                    gross = int(grossStr[1:].replace(',',''))
                    return gross
                else:
                    gross = grossStr.replace(u'\xa0', u' ')
                    return int(gross[gross.find(' ')+1:].replace(',', ''))
        
        return None
    
    except:
        print('Could not parse gross for id ' + id)
        return None