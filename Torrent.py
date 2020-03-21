import settings


class Torrent:
    def __init__(self, rss):
        self.title = rss['title']
        self.link = rss['link']
        self.summary = rss['summary']
        self.size = self.summary.split('/ ')[2].split(' ')[0]
        self.download = float(self.size) <= settings.MAX_SIZE | settings.MAX_SIZE == -1
        self.id = int(rss['comments'].split('/')[-1])
