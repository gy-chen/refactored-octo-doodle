import urllib.request
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Text
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship
from lxml import etree

engine = create_engine('mysql+mysqlconnector://root@localhost/feeds')
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Feed(Base):
    __tablename__ = 'feeds'

    id = Column(Integer, primary_key=True)
    url = Column(String(250))
    title = Column(String(100))
    description = Column(Text)

    items = relationship('FeedItem')


class FeedItem(Base):
    __tablename__ = 'feeditems'

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    description = Column(Text)
    link = Column(String(250))
    feed_id = Column(Integer, ForeignKey('feeds.id'))

    feed = relationship('Feed', back_populates='items')

class Getter:
    """Get RSS feed from the given url.
    """
    def __init__(self, url):
        self._url = url

    def get_rss_file(self):
        "Get file like object that contains RSS feed content"
        return urllib.request.urlopen(self._url)


class Parser:
    """Generate Feed and FeedItem instances from the given RSS content.
    """
    def __init__(self, file, feed_url):
        self._file = file
        self._feed_url = url

    def get_feed(self):
        tree = etree.parse(self._file)
        root = tree.getroot()
        feed = Feed()
        feed.url = self._feed_url
        channel = root.find('channel')
        title = channel.find('title')
        feed.title = title.text
        description = channel.find('description')
        feed.description = description.text
        items = channel.findall('item')
        feed.items = []
        for item in items:
            feeditem = FeedItem()
            feeditem.title = item.find('title').text
            feeditem.link = item.find('link').text
            feeditem.description = item.find('description').text
            feed.items.append(feeditem)
        return feed


Base.metadata.create_all(engine)

if __name__ == '__main__':
    url = 'http://www.howstuffworks.com/podcasts/stuff-you-should-know.rss'
    getter = Getter(url)
    parser = Parser(getter.get_rss_file(), url)
    feed = parser.get_feed()
