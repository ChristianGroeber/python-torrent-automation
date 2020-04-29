# python-torrent-automation
A script that watches an RSS feed from DXDHD and automatically downloads to .torrent files if specific criteria are met

## Prerequisits
*  Python 3
*  TKinter ([Windows](https://tkdocs.com/tutorial/install.html#installwin)|[Linux](https://stackoverflow.com/a/4784123))
*  feedparser (```pip3 install feedparser```)

## Installation
*  clone the repository

## Setup
*  Find an RSS Feed on DXDHD or any other tracker you'd like to use to fetch torrents (app is developed for rss feeds from dxdhd so it may not work with other trackers)
*  create a copy of the ```.env``` file and name it ```.env.local```
*  change the values in ```.env.local``` to your requirements (those can later be changed during runtime)
*  define a directory in your torrent client to watch for newly added *.torrent files

## Usage
*  run ```main.py``` (```python3 main.py```)

## Run without GUI
*  add ```--nogui``` after the beforementioned command. (```python3 main.py --nogui```)
*  You will be asked if you wish to change any of the options, if you're happy with the default just press enter.