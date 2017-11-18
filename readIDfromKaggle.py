import urllib.request  as urllib2 
from bs4 import BeautifulSoup
import csv

def readIdsFromKaggle():
    IDs=[]


    with open('imdb.csv') as f:
        lines = f.readlines()
        for i in range(1, len(lines)):
            line = lines[i]
            words = line.split(',')
            IDs.append(words[1])
    return IDs