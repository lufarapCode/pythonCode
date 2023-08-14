"""
Scraping GitHub Profile using Python
When we open any GitHub account, we see a profile picture, the name of the user, and a short description of 
the user in the profile section. Here you will learn how to scrape your GitHub profile image. For this task, 
you need some knowledge of HTML and the requests and BeautifulSoup libraries in Python.

If you have never used the BeautifulSoup library before, use the command mentioned below in your command prompt 
or terminal to install this library in your Python virtual environment:

pip install beautifulsoup4
"""

import requests
from bs4 import BeautifulSoup as bs

github_profile = "https://github.com/amankharwal"
req = requests.get(github_profile)
scraper = bs(req.content, "html.parser")
profile_picture = scraper.find("img", {"alt": "Avatar"})["src"]
print(profile_picture)