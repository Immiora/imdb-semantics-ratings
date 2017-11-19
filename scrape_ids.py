import urllib.request as urllib2
from bs4 import BeautifulSoup
from readIDfromKaggle import *
from synopsis import *
import sys
import datetime


startYear = int(sys.argv[1])
endYear = int(sys.argv[2])

keggleIds = readIdsFromKaggle();

# mainUrl = 'http://www.imdb.com/year'

# mainPage = urllib2.urlopen(mainUrl)
# mainSoup = BeautifulSoup(mainPage, 'html.parser')

idsWithSynopsisNotInKaggleDb = []

# yearsTable = mainSoup.find('table', {'class':'splash'}).find_all('a');

i = 0

# http://www.imdb.com/search/title?release_date=2010&sort=user_rating,asc&ref_=rlm_yr
for year in range(startYear, endYear):
    # entry = yearsTable[iEntry]
    print('At year ' + str(year))
    yearUrl = 'http://www.imdb.com/search/title?release_date=' + str(year) + '&sort=user_rating,asc&ref_=rlm_yr'
    yearPage = urllib2.urlopen(yearUrl)
    yearSoup = BeautifulSoup(yearPage, 'html.parser')
    movieList = yearSoup.find_all('img', {'class': 'loadlate', 'height':'98'})
    for entry in movieList:
        i = i + 1
        newId = entry['data-tconst']
        if newId not in keggleIds:
            syn = get_synopsis(newId)
            if syn is not None:
                idsWithSynopsisNotInKaggleDb.append([newId, syn])
                print(str(i) + ': ' + 'new id: ' + newId)
                idsWithSynopsisNotInKaggleDb.append(newId)
            else:
                print(str(i) + ': ' + 'synopsis not available')
        else:
            print(str(i) + ': ' + 'id already in db')

timeStr = str(datetime.date.today().strftime("%I-%M-%S"))
theFile = open('new_IDs_startyear_' + str(startYear) + '_endyear_' + str(endYear) + '_' + timeStr + '.txt', 'w')
for id in idsWithSynopsisNotInKaggleDb:
    theFile.write("%s\n" % id)