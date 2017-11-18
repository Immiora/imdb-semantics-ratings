import re

TAG_RE = re.compile(r'<[^>]+>')

def remove_tags(text):
    return TAG_RE.sub('', text)

def id_to_main_page_url(id):
    return 'http://www.imdb.com/title/' + id + '/?ref_=tt_rec_tti'