import json
import requests

class Scraper(object):
    def __init__(self, url):
        self.url = url

    def scrape_site(self):
        text = requests.get(self.url).text
        content_to_search = "<meta content=\""
        start_index = text.find(content_to_search)
        likes_word_index = text.find("Likes", start_index)
        if likes_word_index == -1:
            return -1
        return text[(start_index + len(content_to_search)):likes_word_index]