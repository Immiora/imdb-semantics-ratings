import urllib.request  as urllib2 
from bs4 import BeautifulSoup
from utils import *

def parse_budget(xmlFile, id):
    try:
        for h4 in xmlFile.find_all('h4'):
            if "Budget:" in h4:
                budgetStr = h4.next_sibling.strip()
                if budgetStr[0] == '$':
                    budget = int(budgetStr[1:].replace(',',''))
                    return budget
                else:
                    budget = budgetStr.replace(u'\xa0', u' ')
                    return int(budget[budget.find(' ')+1:].replace(',', ''))
        
        return None
       
    
    except:
        print('Could parse budget for id ' + id)
        return None

