import urllib.request as urllib2
from bs4 import BeautifulSoup
from readIDfromKaggle import *
from synopsis import *
import sys
import datetime


startYear = int(sys.argv[1])
endYear = int(sys.argv[2])

keggleIds = readIdsFromKaggle();

idsWithSynopsisNotInKaggleDb = []
i = 0
maxBatch = 7
for year in range(startYear, endYear):
    print('At year ' + str(year))
    iBatch = 2
    while True:
        print('\tAt batch ' + str(iBatch - 1))
        url = 'http://www.imdb.com/search/title?release_date=' + str(year) + '&sort=user_rating,asc&page=' + str(iBatch) + '&ref_=adv_nxt'
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        movieList = soup.find_all('img', {'class': 'loadlate', 'height':'98'})
        if (len(movieList) == 0 or iBatch == maxBatch):
            break
        iBatch = iBatch + 1
        for entry in movieList:
            i = i + 1
            newId = entry['data-tconst']
            if newId not in keggleIds:
                syn = get_synopsis(newId)
                if syn is not None:
                    idsWithSynopsisNotInKaggleDb.append([newId, syn])
                    print('\t\t' + str(i) + ': ' + 'new id: ' + newId)
                    idsWithSynopsisNotInKaggleDb.append(newId)
                else:
                    print('\t\t' + str(i) + ': ' + 'synopsis not available')
            else:
                print('\t\t' + str(i) + ': ' + 'id already in db')

timeStr = str(datetime.date.today().strftime("%I-%M-%S"))
theFile = open('new_IDs_startyear_' + str(startYear) + '_endyear_' + str(endYear) + '_' + timeStr + '.txt', 'w')
for id in idsWithSynopsisNotInKaggleDb:
    theFile.write("%s\n" % id)