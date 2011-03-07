import urllib2, urllib, webbrowser
from BeautifulSoup import BeautifulSoup
import re
import difflib

def removeTags(thing):
    for tag in thing.findAll(True): tag.replaceWith(tag.renderContents())

def unescape(s):
  s = s.replace("&lt;", "<")
  s = s.replace("&gt;", ">")
  # this has to be last:
  s = s.replace("&amp;", "&")
  s = s.replace("&nbsp;", " ")
  return s
    
def removeHTML(string):
    return re.sub("<(.|\n)*?>", "", string)
    
def cleanString(string):
    return removeHTML(string).strip()

def noms():
        print 'Downloading page...'
        page = urllib2.urlopen("http://www.dartmouth.edu/dining/")
        print 'Page downloaded.'
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
                    for foodItem in unescape(parts[1]).replace(";",",").split(","):
                        noms.append((cleanString(foodItem), cleanString(category), currentPlace))
        print 'Page parsed.'
        return noms

def stringInString(needle, haystack):
    return haystack.lower().find(needle.lower()) > -1

def close_match(stringA, stringB):
	return len(difflib.get_close_matches(stringA, [stringB])) > 0

def removePunctuation(text):
	return re.sub("\s+", "", re.sub("[^A-z0-9]","",text))

noms = noms()
        
def isThere(nomName):
    global noms
    def isRightNom(x): return stringInString(removePunctuation(nomName),removePunctuation(x[0]))
    return filter(isRightNom, noms)