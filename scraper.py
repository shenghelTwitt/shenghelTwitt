import urllib2
from BeautifulSoup import BeautifulSoup
import pickle
import os
global opener
global cookie

def start():
	global cookie
	cookie = pickle.load(open("cookie.st", "rb"))
	opener = setup_opener()

def setup_opener():
	global cookie
	proxy = urllib2.ProxyHandler({'https': '127.0.0.1:8580'})
	opener = urllib2.build_opener(proxy)
	urllib2.install_opener(opener)

	opener.addheaders.append(('Cookie', 'auth_token=' + cookie))
	return opener


class User:
	def get_twitt(self,name = ''):
		profile = opener.open('https://twitter.com/'+name)
		prohttp = profile.read()
		soup = BeautifulSoup(prohttp)
		twitt = soup.findAll('p',{'class':'ProfileTweet-text js-tweet-text u-dir','lang':'en','data-aria-label-part':'0','dir':'ltr'})
		for i in range(len(twitt)):
			twitt[i] = twitt[i].text
		return twitt

	def get_flwing(self,name = ''):
		profile = opener.open('https://twitter.com/' + name + '/following')
		prohttp = profile.read()
		soup = BeautifulSoup(prohttp)
		flwing = soup.findAll('span',{'class':'u-linkComplex-target'})
		del flwing[0]
		del flwing[1]
		for i in range(len(flwing)):
			flwing[i] = flwing[i].text
		return flwing
	def get_flwer(self,name = ''):
		profile = opener.open('https://twitter.com/' + name + '/followers')
		prohttp = profile.read()
		soup = BeautifulSoup(prohttp)
		flwer = soup.findAll('span',{'class':'u-linkComplex-target'})
		del flwer[0]
		del flwer[1]
		for i in range(len(flwer)):
			flwer[i] = flwer[i].text
		return flwer
	def __init__(self,name = ''):
		self.name = name
		#self.flwing = self.get_flwing(name)
		self.attraction = [0,0]
	def obj_flwing(self):
		objList = []
		for i in self.flwing:
			objList.append(i)
		return objList
