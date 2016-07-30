from flask import Flask
from flask import request
from flask import make_response
from flask import jsonify
from flask_cors import CORS
import feeds

app = Flask(__name__)
CORS(app)

@app.route('/feeds/add', methods=['POST'])
def feed_add():
    url = request.form['url']
    getter = feeds.Getter(url)
    parser = feeds.Parser(getter.get_rss_file(), url)
    feed = parser.get_feed()
    session = feeds.Session()
    session.add(feed)
    session.commit()
    return make_response('', 200)

@app.route('/feed/<int:feed_id>', methods=['GET'])
def get_feed(feed_id):
    # TODO use factory class to hide query detail
    session = feeds.Session()
    feed = session.query(feeds.Feed).filter(feeds.Feed.id == feed_id).one()
    feed_dict = {}
    feed_dict['id'] = feed.id
    feed_dict['title'] = feed.title
    feed_dict['description'] = feed.description
    items = []
    for item in feed.items:
        item_dict = {}
        item_dict['id'] = item.id
        item_dict['title'] = item.title
        item_dict['description'] = item.description
        item_dict['link'] = item.link
        items.append(item_dict)
    feed_dict['items'] = items
    return jsonify(feed=feed_dict)

@app.route('/feeds', methods=['GET'])
def get_feeds():
    # TODO use factory class to hide query detail
    session = feeds.Session()
    feeds_dict = []
    for feed in session.query(feeds.Feed).all():
        feed_dict = {}
        feed_dict['id'] = feed.id
        feed_dict['title'] = feed.title
        feed_dict['description'] = feed.description
        items = []
        for item in feed.items:
            item_dict = {}
            item_dict['id'] = item.id
            item_dict['title'] = item.title
            item_dict['description'] = item.description
            item_dict['link'] = item.link
            items.append(item_dict)
        feed_dict['items'] = items
        feeds_dict.append(feed_dict)
    return jsonify(feeds=feeds_dict)
