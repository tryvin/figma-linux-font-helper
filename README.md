# figma-linux-font-helper
Figma Linux Font Helper

# Why

A fellow friend of mine was switching to Linux, and needed the Local fonts support for Figma

# How

This project was a reverse engineer from the local font helper from Figma for App, it uses fc-list, and fc-cache for the fonts lists, and python for the webserver

# How to use it

* Install Python3 and Pip3 (Pip for Python3)
* Run `sudo pip3 install -r requirements.txt`
* Run `python3 server.py`
* Navigate to figma.com and try to use the local fonts.


# Docker-compose

You can also use `docker-compose` in order to run it as a container, simply run `docker-compose up` and let docker do it's magic

There's also a environment variable in the compose file, called `FONTS_FOLDER`, use this variable if your font folder is mapped somewhere else, for example, on OSX you might want to use `FONT_FOLDER=~/Library/Fonts docker-compose up`

Rename `.env.example` to `.env` to define a custom value to `FONTS_FOLDER` before build your containers with `docker-compose`.


# Big Thanks

Big Thanks to the following contributors for improving this project! (NOT sorted by order of importance)

* [arpanetus](https://github.com/arpanetus)
* [aanpilov](https://github.com/aanpilov)
* [marcosfreitas](https://github.com/marcosfreitas)
* Wayne Steidley
