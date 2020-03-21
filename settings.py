from pathlib import Path
import os


# where .torrent files should be copied, default value: /home/$USER/rtorrent/watch/start/
WATCH_DIR = os.path.join(str(Path.home()), 'rtorrent/watch/start/')

# the maximum size allowed to download. set to -1 to ignore
MAX_SIZE = 50
