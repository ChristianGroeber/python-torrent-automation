import feedparser
import Torrent
import urllib.request
import os
import settings


news_feed = feedparser.parse('https://dxdhd.com/rss/217.c4233ae8c9619dbb8f1c1a6cd5ab34df')

torrents = []


def download(torrent):
    urllib.request.urlretrieve(torrent.link, os.path.join(settings.WATCH_DIR, str(torrent.id) + ".torrent"))


for torr in news_feed.entries:
    parsed = Torrent.Torrent(torr)
    if parsed.download:
        for torrent in torrents:
            if torrent.id is parsed.id:
                break
        else:
            torrents.append(parsed)
            download(parsed)
