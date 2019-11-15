from flask import Flask, render_template, request
from scraper import Scraper

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/', methods=['POST'])
def get_likes():
    scraper = Scraper(request.form["url"])
    num_likes = scraper.scrape_site()
    if num_likes == -1:
        num_likes = "Sorry, this account is private"
    num_likes = "Number of likes: " + num_likes
    return render_template("home.html", num_likes=num_likes)

if __name__ == '__main__':
    app.run()