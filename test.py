#!/usr/bin/env python3

from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

def getTitle(url):
	try:
		htmlFile = urlopen(url)
	except HTTPError as e:
		print(e)
		quit()
	except URLError as u:
		print("No Server")

	try:
		bsObj = BeautifulSoup(htmlFile.read(), "html.parser")
		title = bsObj.head.title
	except AttributeError as a:
		return None
	return title

t = getTitle("https://www.espn.com")

if t == None:
	print("No Title")
else:
	print(t)

