# python-torrent-automation
A script that watches an RSS feed from DXDHD and automatically downloads to .torrent files if specific criteria are met

## Prerequisits
*  Python 3
*  TKinter ([Windows](https://tkdocs.com/tutorial/install.html#installwin)|[Linux](https://stackoverflow.com/a/4784123))
*  feedparser (```pip3 install feedparser```)

## Installation
*  clone the repository

## Setup
*  Find an RSS Feed on DXDHD you'd like to use to fetch torrents
*  create a copy of the ```.env``` file and name it ```.env.local```
*  change the values in ```.env.local``` to your requirements (those can later be changed during runtime)
*  define a directory in your torrent client to watch for newly added *.torrent files

## Usage
*  run ```main.py``` (```python3 main.py```)
