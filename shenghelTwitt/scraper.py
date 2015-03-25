import urllib2
from BeautifulSoup import BeautifulSoup
import pickle
import os
global opener
global cookie
# -*- coding: utf-8 -*-
def start():
	global cookie
	global opener
	file_cookie = open("cookie.st", "rb")
	cookie = pickle.load(file_cookie)
	file_cookie.close()
	#print "in start of scraper"
	opener = setup_opener()

def setup_opener():
	global cookie
	global opener
	#proxy = urllib2.ProxyHandler({'https': '127.0.0.1:8080'})
	#opener = urllib2.build_opener(proxy)
	opener = urllib2.build_opener()
	urllib2.install_opener(opener)

	opener.addheaders.append(('Cookie', 'auth_token=' + cookie))
	#print "salam"
	return opener


class User:
	global opener
	def get_twitt(self):
		profile = opener.open('https://twitter.com/'+self.name)
		prohttp = profile.read()
		soup = BeautifulSoup(prohttp)
		twitt = soup.findAll('p',{'class':'ProfileTweet-text js-tweet-text u-dir','lang':'en','data-aria-label-part':'0','dir':'ltr'})
		for i in range(len(twitt)):
			#print "###",twitt[i].text
			twitt[i] = str( twitt[i].text.encode("ascii","ignore"))
			#twitt[i] = str(twitt[i].text)
			#print "@@@",twitt[i]
		return twitt

	def get_flwing(self):
		profile = opener.open('https://twitter.com/' + self.name + '/following')
		prohttp = profile.read()
		soup = BeautifulSoup(prohttp)
		flwing = soup.findAll('span',{'class':'u-linkComplex-target'})
		del flwing[0]
		del flwing[0]
		for i in range(len(flwing)):
			flwing[i] = str(flwing[i].text)
			
		return flwing
	def get_flwer(self):
		profile = opener.open('https://twitter.com/' + self.name + '/followers')
		prohttp = profile.read()
		soup = BeautifulSoup(prohttp)
		flwer = soup.findAll('span',{'class':'u-linkComplex-target'})
		del flwer[0]
		del flwer[0]
		for i in range(len(flwer)):
			flwer[i] = str(flwer[i].text)
		return flwer
	def __init__(self,name = ''):
		self.name = name
		#self.flwing = self.get_flwing(name)
		followingUsernames = []
		self.attraction = [0, 0, 0] #[FOOTBALL/ALL, PROGRAMMING/ALL, ALL]
	def __str__(self):
		return self.name + " :" + str(self.attraction)
