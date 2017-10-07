from lxml import html
import requests

BASE_URL = 'https://hypem.com/popular/'
PAGES = [1,2,3]

def scrape_HTML(path):
    page = requests.get(path)
    tree = html.fromstring(page.content)
    
    tracks = tree.xpath('//a[@rel="nofollow"]')
    return [i.attrib['href'].split('/')[3] for i in tracks if i.text=='Spotify']

def generate_tracklist():
    track_IDs = []
    for i in PAGES:
        track_IDs += scrape_HTML(BASE_URL + str(i))

    return track_IDs

