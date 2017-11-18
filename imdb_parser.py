import urllib.request  as urllib2 
from bs4 import BeautifulSoup
from parse_title import *
from parse_cast import *
from parse_director import *
from readIDfromKaggle import *
import pandas as pd
 
raw_ids = readIdsFromKaggle()
titles = [];

id = raw_ids[0]
url = id_to_main_page_url(id)
page = urllib2.urlopen(url)
xmlFile = BeautifulSoup(page, 'html.parser')
titleStr = parse_title(xmlFile)
parse_cast(xmlFile)
parse_director(xmlFile)
print(titleStr)
titles.append(titleStr)


# dataFrame = pd.DataFrame({'titles': titles, 'id': ids})
# dataFrame.to_csv('titles.csv', sep=';')

