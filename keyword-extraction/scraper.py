from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import urllib2
from BeautifulSoup import BeautifulSoup

userName = 'armanjtehrani'#raw_input('please enter your user name & password: \n')
passWord = 'POISALA'#raw_input()
browser = webdriver.Firefox()
browser.get("http://www.twitter.com")
username = browser.find_element_by_id("signin-email")
password = browser.find_element_by_id("signin-password")

username.send_keys(userName)
password.send_keys(passWord,Keys.ENTER)
cookies = browser.get_cookies()
for i in cookies :
    if i['name'] == 'auth_token' :
        value = str(i['value'])
        break
def setup_opener():
    proxy = urllib2.ProxyHandler({'https': '127.0.0.1:8580'})
    opener = urllib2.build_opener(proxy)
    urllib2.install_opener(opener)

    opener.addheaders.append(('Cookie', 'auth_token=' + value))
    return opener
opener = setup_opener()
class Profile:
    def get_twitt(self):
        profile = opener.open('https://twitter.com/'+self.name)
        prohttp = profile.read()
        soup = BeautifulSoup(prohttp)
        twitt = soup.findAll('p',{'class':'ProfileTweet-text js-tweet-text u-dir','lang':'en','data-aria-label-part':'0','dir':'ltr'})
        for i in range(len(twitt)):
            twitt[i] = twitt[i].text
        return twitt

    def get_flwing(self):
        profile = opener.open('https://twitter.com/' + self.name + '/following')
        prohttp = profile.read()
        soup = BeautifulSoup(prohttp)
        flwing = soup.findAll('span',{'class':'u-linkComplex-target'})
        for i in range(len(flwing)):
            flwing[i] = flwing[i].text
        return flwing
    def get_flwer(self):
        profile = opener.open('https://twitter.com/' + self.name + '/followers')
        prohttp = profile.read()
        soup = BeautifulSoup(prohttp)
        flwer = soup.findAll('span',{'class':'u-linkComplex-target'})
        for i in range(len(flwer)):
            flwer[i] = flwer[i].text
        return flwer
    def __init__(self,name=""):
        self.name = name
    #    self.rel = rel
     #   self.twitt = self.get_twitt(name)
      #  self.flwing = self.get_flwing(name)
       # self.flwer = self.get_flwer(name)
        self.attract = None #[football, programming, totalTwittCount]


myPro = Profile()
pro = []

for i in range(len(myPro.flwing)):
    pro.append(Profile(myPro.flwing[i],userName))
    pause = False
for user in pro:
    while not pause:
        #milad(user)
        for i in range(len(user.flwing)):
            for j in pro:
                if j.name == user.flwing[i]:
                    j.rel.append(user.name)
                    break
            else: 
                pro.append(Profile(user.flwing[i],))

        
