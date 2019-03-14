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
