from flask import Flask, render_template, request
import json
import os
from communities.CommunitiesFacade import CommunitiesFacade
from topics.TopicsFacade import TopicsFacade

app = Flask(__name__)
app.debug = True
communitiesFacade = CommunitiesFacade()
topicsFacade = TopicsFacade()


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
def home_page():
    topics = {
        "music": topicsFacade.get_topics("music"),
        "books": topicsFacade.get_topics("books"),
        "news": topicsFacade.get_topics("news")
    }
    return render_template('index.html', topics=topics)


@app.route('/topic/<topic>')
def topic_page(topic):
    community_comments = communitiesFacade.search_comments(topic)
    community_pages = []#communitiesFacade.search_pages(topic)
    return render_template('topic.html', topic=topic, community_comments=community_comments,
                           community_pages=community_pages)


@app.route('/search')
def search():
    return json.dumps(communitiesFacade.search_comments(request.args.get('search_terms')))


if __name__ == '__main__':
    app.run()
