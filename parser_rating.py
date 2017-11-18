import urllib.request as urllib2
from urllib.request import HTTPError
from bs4 import BeautifulSoup


def get_ratingvalue(id_):
    quote_page = 'http://www.imdb.com/title/%s/' %id_
    try:
        page = urllib2.urlopen(quote_page)
    except HTTPError:
        return None

    page = urllib2.urlopen(quote_page)
    return BeautifulSoup(page, 'html.parser')


def get_rating(soup):
    file = get_ratingvalue(soup)
    return float(file.find("div", {"class":"ratingValue"}).find("span").text)


def loop_ratings(id_list):
    ratings = []
    for id_ in id_list:
        rate = get_rating(id_)
        if rate is not None:
            ratings.append(rate)

    return ratings
