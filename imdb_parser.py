import urllib.request as urllib2
from bs4 import BeautifulSoup
from parse_title import *
from parse_cast import *
from parse_director import *
from parse_writers import *
from readIDfromKaggle import *
import pandas as pd
 
raw_ids = readIdsFromKaggle()
titles = [];

id = raw_ids[0]
# url = id_to_main_page_url(id)
url = 'http://www.imdb.com/title/tt2015381/?ref_=tt_rec_tti'
page = urllib2.urlopen(url)
xmlFile = BeautifulSoup(page, 'html.parser')
titleStr = parse_title(xmlFile)
parse_cast(xmlFile)
print(parse_director(xmlFile))
print(parse_writers(xmlFile))
print('title: ' + titleStr)
titles.append(titleStr)


# dataFrame = pd.DataFrame({'titles': titles, 'id': ids})
# dataFrame.to_csv('titles.csv', sep=';')

<<<<<<< HEAD
parse_budget()
=======
>>>>>>> d8ce60e7b99c6b5800926671f48124baa1bbbcb8
