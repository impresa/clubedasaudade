from flask import Flask, render_template, request
import requests
import json
import os
from requests_oauthlib import OAuth1
from communities.CommunitiesFacade import CommunitiesFacade

app = Flask(__name__)
app.debug = True
communitiesFacade = CommunitiesFacade()


@app.url_defaults
def hashed_url_for_static_file(endpoint, values):
    if 'static' == endpoint or '.static' == endpoint[-7:]:
        filename = values.get('filename', None)
        if filename:
            if request.blueprint is None:
                static_folder = app.static_folder
            else:
                static_folder = app.blueprints[request.blueprint].static_folder

            param_name = 'h'
            while param_name in values:
                param_name = '_' + param_name

            values[param_name] = static_file_hash(os.path.join(static_folder, filename))

def static_file_hash(filename):
    return int(os.stat(filename).st_mtime)


@app.route('/')
def index_page():
    return render_template('index.html')


@app.route('/search')
def search():
    return json.dumps(communitiesFacade.search(request.args.get('search_terms')))


if __name__ == '__main__':
    app.run()
