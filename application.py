from flask import Flask, render_template
import requests
from requests_oauthlib import OAuth1

app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template('index.html')

@app.route('/search')
def hello_world():
    url = 'https://api.twitter.com/1.1/search/tweets.json?q=%23charliehebdo&lang=pt'
    auth = OAuth1('hxyttWQ5OuciWPJdBJgntZ3UO', 'oJFPWpLuuNM3hjfpTLhKCMOdjHo5gQktdzTfEK5BaetznEn5dK',
                  '22373407-72aJvjhjUH7BZ3J9kJjeuv0wrWBWh4cRxCfNUGG89', 'zA3YWLSxJr0BgvGnh5Ca9QXKhiumSUyTi5pYvxUJ7nNvh')
    r=requests.get(url, auth=auth)
    return r.text

if __name__ == '__main__':
    app.run()
