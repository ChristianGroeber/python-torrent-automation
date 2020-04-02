import os
import sched
import time
import urllib.request
from tkinter import *
import threading
import datetime

import feedparser

import Torrent
import settings
import sys

gui = True
master = None

if len(sys.argv) > 1 and sys.argv[1] == '--nogui':
    gui = False

pause_btn_text = StringVar()
pause_btn_text.set('Start')

torrents = []
all_torrents = []

schedule = sched.scheduler(time.time, time.sleep)

updates = 1
log_file = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + ".log"

started = False


def get_time_str():
    return datetime.datetime.now().strftime('%H:%M:%S')


def update_settings():
    new_watch_dir = watch_dir.get()
    if new_watch_dir != settings.WATCH_DIR:
        write_log('updated watch dir to' + new_watch_dir)
        settings.WATCH_DIR = new_watch_dir

    new_rss_feed = rss_feed.get()
    if new_rss_feed != settings.RSS_FEED:
        write_log('updated rss feed to ' + new_rss_feed)
        settings.RSS_FEED = new_rss_feed

    new_update_after_minutes = float(update_after_minutes.get())
    if new_update_after_minutes != settings.UPDATE_AFTER_MINUTES:
        write_log('updated update after minutes to ' + str(new_update_after_minutes))
        settings.UPDATE_AFTER_MINUTES = new_update_after_minutes

    new_max_size = int(max_size.get())
    if new_max_size != settings.MAX_SIZE:
        write_log('updated max size to ' + str(new_max_size))
        settings.MAX_SIZE = new_max_size


def toggle_active():
    global started
    if not started:
        started = True
        pause_btn_text.set('Pause')
        create_thread()
    elif settings.AUTOMATIC_UPDATE:
        settings.AUTOMATIC_UPDATE = False
        pause_btn_text.set('Continue')
    else:
        settings.AUTOMATIC_UPDATE = True
        pause_btn_text.set('Pause')
        create_thread()


def download(torrent):
    write_log('downloading ' + torrent.title)
    urllib.request.urlretrieve(torrent.link, os.path.join(settings.WATCH_DIR, str(torrent.id) + ".torrent"))


def update(sc, update_counter):
    write_log('running update ' + str(update_counter))
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
    write_log("finished running update " + str(update_counter))
    update_counter += 1
    global updates
    updates = update_counter

    if settings.AUTOMATIC_UPDATE:
        schedule.enter(60 * settings.UPDATE_AFTER_MINUTES, 1, update, (sc, update_counter))


def download_manually():
    global manual_download
    url = manual_download.get()
    torrent = Torrent.Torrent({'title': url, 'link': url, 'summary': '0 / 0 / 0 GiB', 'comments': url.split('/')[-1].split('.')[0]})
    download(torrent)


def create_thread():
    thread = threading.Thread(target=schedule.run, args=(1,))
    schedule.enter(1, 1, update, (schedule, updates))
    thread.start()
    return thread


master = Tk()


def close():
    master.destroy()
    raise Exception


if gui:
    Label(master, text="Watch Directory").grid(row=0)
    Label(master, text="Update Every Minutes").grid(row=1)
    Label(master, text="RSS Feed").grid(row=2)
    Label(master, text="Max Size").grid(row=3)
    Label(master, text="Manual download").grid(row=4)

    watch_dir = Entry(master)
    update_after_minutes = Entry(master)
    rss_feed = Entry(master)
    max_size = Entry(master)

    manual_download = Entry(master)

    watch_dir.grid(row=0, column=1)
    update_after_minutes.grid(row=1, column=1)
    rss_feed.grid(row=2, column=1)
    max_size.grid(row=3, column=1)

    manual_download.grid(row=4, column=1)

    watch_dir.insert(END, settings.WATCH_DIR)
    update_after_minutes.insert(END, settings.UPDATE_AFTER_MINUTES)
    rss_feed.insert(END, settings.RSS_FEED)
    max_size.insert(END, settings.MAX_SIZE)

    update_btn = Button(master, text='Update', command=update_settings)
    update_btn.grid(row=5, column=1)
    pause_btn = Button(master, textvariable=pause_btn_text, command=toggle_active)
    pause_btn.grid(row=6, column=1)

    download_btn = Button(master, text='Download', command=download_manually)
    download_btn.grid(row=4, column=2)

    log_area = Text(master)
    log_area.grid(row=7, column=1)
    log_area.config(state=DISABLED)


def write_log(text):
    global log_file
    global log_area
    text = get_time_str() + ': ' + str(text) + '\n'
    if gui:
        log_area.config(state=NORMAL)
        log_area.insert(INSERT, text)
        log_area.config(state=DISABLED)
    else:
        print(text)


if gui:
    master.protocol("WM_DELETE_WINDOW", close)
    master.mainloop()
else:
    rss_feed = input('rss feed [' + settings.RSS_FEED + "]: ")
    watch_dir = input('rss feed [' + settings.WATCH_DIR + "]: ")
    update_after_minutes = input('rss feed [' + str(settings.UPDATE_AFTER_MINUTES) + "]: ")
    automatic_update = input('rss feed [' + settings.AUTOMATIC_UPDATE + "] - y/n: ")

    if rss_feed != '':
        settings.RSS_FEED = rss_feed
    if watch_dir != '':
        settings.WATCH_DIR = watch_dir
    if update_after_minutes != '':
        settings.WATCH_DIR = update_after_minutes
    if automatic_update != '':
        settings.AUTOMATIC_UPDATE = automatic_update

    create_thread()
