import feedparser
import Torrent
import urllib.request
import os
import settings
import sched, time


schedule = sched.scheduler(time.time, time.sleep)
torrents = []
all_torrents = []


def download(torrent):
    print('adding torrent ' + torrent.title)
    urllib.request.urlretrieve(torrent.link, os.path.join(settings.WATCH_DIR, str(torrent.id) + ".torrent"))


def update(sc, update_counter):
    print('Running update ' + str(update_counter))
    news_feed = feedparser.parse(settings.RSS_FEED)
    for torr in news_feed.entries:
        parsed = Torrent.Torrent(torr)
        all_torrents.append(parsed)
        if parsed.download:
            for torrent in torrents:
                if torrent.id == parsed.id:
                    break
            else:
                torrents.append(parsed)
                download(parsed)
    print('finished update ' + str(update_counter))
    if settings.AUTOMATIC_UPDATE:
        update_counter += 1
        schedule.enter(60 * settings.UPDATE_AFTER_MINUTES, 1, update, (sc, update_counter))


schedule.enter(1, 1, update, (schedule, 1))
schedule.run()
