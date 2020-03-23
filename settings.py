import os
from envParser import EnvParser

parser = EnvParser()
parser.parse()

# where .torrent files should be copied, default value: /home/$USER/rtorrent/watch/start/
WATCH_DIR = parser.get('WATCH_DIR')

# the maximum size allowed to download. set to -1 to ignore default: 50GiB
MAX_SIZE = int(parser.get('MAX_SIZE'))

# if the program should run in a loop
AUTOMATIC_UPDATE = int(parser.get('AUTOMATIC_UPDATE')) == 1

# after how many minutes the program should rerun; default: 30
UPDATE_AFTER_MINUTES = float(parser.get('UPDATE_AFTER_MINUTES'))

# url of rss feed
RSS_FEED = parser.get('RSS_FEED')
