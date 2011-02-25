# INTENSE SCRAPING ACTION BY JAMES
#!/usr/bin/env python

import urllib2, urllib, webbrowser
from BeautifulSoup import BeautifulSoup
import re

def removeTags(thing):
	for tag in thing.findAll(True): tag.replaceWith(tag.renderContents())

def entities(string):
	return re.sub("&nbsp;", " ", re.sub("&amp;", "&", string))
	
def removeHTML(string):
	return re.sub("<(.|\n)*?>", "", string)
	
def cleanString(string):
	return entities(removeHTML(string)).strip()

def noms():
		page = urllib2.urlopen("http://www.dartmouth.edu/dining/")
		soup = BeautifulSoup(page)
		sidebar = soup.find("div", {"class":"a1"})
		noms = []
		currentPlace = ""
		for thing in sidebar.findAll():
			if (thing.name == 'h2'):
				removeTags(thing)
				currentPlace = thing.renderContents()
			elif (thing.name == 'li'):
				parts = thing.renderContents().split(":")
				if (len(parts) > 1):
					category = parts[0]
					for foodItem in parts[1].replace(";",",").split(","):
						noms.append((cleanString(foodItem), cleanString(category), currentPlace))
		return noms

def stringInString(needle, haystack):
	return haystack.lower().find(needle.lower()) > -1

noms = noms()
		
def isThere(nomName):
	global noms
	def isRightNom(x): return stringInString(nomName,x[0])
	return filter(isRightNom, noms)

print isThere("chicken")
