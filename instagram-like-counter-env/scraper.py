import json
import requests

from bs4 import BeautifulSoup

class Scraper(object):
    def __init__(self):
        #self.url = "https://www.instagram.com/p/B4SDBGCHL6y/"
        print("Insert url of public picture")
        self.url = input()

    def scrape_site(self):
        text = requests.get(self.url).text
        content_to_search = "<meta content=\""
        start_index = text.find(content_to_search)
        likes_word_index = text.find("Likes", start_index)
        return text[(start_index + len(content_to_search)):likes_word_index]
        
scraper = Scraper()
print()
print("Number of likes: " + scraper.scrape_site())