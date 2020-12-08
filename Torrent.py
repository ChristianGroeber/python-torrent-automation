import settings
import re


class Torrent:
    def __init__(self, rss):
        self.summary = self.parse_summary(rss['summary'])
        self.title = rss['title']
        self.link = rss['links'][1]['href']
        self.size = self.summary['size'].split(' ')[0]
        self.download = float(self.size) <= settings.MAX_SIZE or settings.MAX_SIZE == -1
        self.id = int(rss['links'][0]['href'].split('/')[-1])

    def parse_summary(self, summary):
        cnt = 0
        ret = {}
        regex = r"(\s*?</?[a-zA-Z]*\s?/?>:?\s?)"
        for line in summary.split('\n'):
            line = line.lstrip()
            line = re.split(regex, line)
            if len(line) < 4:
                continue
            ret[line[2].lower()] = line[4]
            cnt += 1
        print(ret)
        return ret
