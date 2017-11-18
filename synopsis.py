from bs4 import BeautifulSoup
from urllib.request import HTTPError
import urllib.request as urllib2


def get_synopsis(id_):
    """
    
    Args:
        id_: str, containing the id of the movie
        url: str, path to the plot summary page
        
    Returns:
        string containing the synopsis
    """
    
    url = 'http://www.imdb.com/title/%s/plotsummary' % id_
    
    try: 
        page = urllib2.urlopen(url)
    except HTTPError:
        return None
    
    soup = BeautifulSoup(page, 'html.parser')
    
    content = soup.find(id="plot-synopsis-content").find("li").text
    
    if content == '\nIt looks like we don\'t have a Synopsis for this title yet. Be the first to contribute! Just click the "Edit page" button at the bottom of the page or learn more in the Synopsis submission guide.\n':
        return None


    
    return soup.find(id="plot-synopsis-content").find("li").text


def get_multiple_synopses(id_list):
    """
    Args:
        id_list: list of strings
        
    Returns: 
        list of strings
    """
    
    synopses = []
    for id_ in id_list:
        syn = get_synopsis(id_)
        if syn is not None:
            synopses.append(syn)
            
    return synopses