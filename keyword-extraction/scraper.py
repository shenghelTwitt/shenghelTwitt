from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import urllib2
import BeautifulSoup

browser = webdriver.Firefox()
browser.get("http://www.twitter.com")
username = browser.find_element_by_id("signin-email")
password = browser.find_element_by_id("signin-password")

username.send_keys("ArmanJTehrani@Outlook.com")
password.send_keys("POISALA",Keys.ENTER)
cookies = browser.get_cookies()
for i in cookies :
    if i['name'] == 'auth_token' :
        value = str(i['value'])
        break
def setup_opener():
    proxy = urllib2.ProxyHandler({'https': '127.0.0.1:8580'})
    opener = urllib2.build_opener(proxy)
    urllib2.install_opener(opener)

    opener.addheaders.append(('Cookie', 'auth_token=c8f9728c372e61ba5703bec8551601e529bb18c4'))
    return opener

class Profile:
    def get_twitt(self,name = None):
        profile = opener.open("https://twitter.com/" + name)
        prohttp = profile.read()
        soup = BeautifulSoup(prohttp)
        twitt = soup.findAll('p',{'class':'ProfileTweet-text js-tweet-text u-dir','lang':'en','data-aria-label-part':'0','dir':'ltr'})
        for i in range(len(twitt)):
            twitt[i] = twitt[i].text
        return twitt

    def get_flwing(self,name = None):
        profile = opener.open("https://twitter.com/" + name + "/following")
        prohttp = profile.read()
        soup = BeautifulSoup(prohttp)
        flwing = soup.findAll('span',{'class':'u-linkComplex-target'})
        for i in range(len(flwing)):
            flwing[i] = flwing[i].text
        return flwing
    def get_flwer(self,name = None):
        profile = opener.open("https://twitter.com/" + name + "/followers")
        prohttp = profile.read()
        soup = BeautifulSoup(prohttp)
    def __init__(self,name = None,rel = None):
        self.name = name
        self.rel = rel
        self.twitt = get_twitt(name)
        self.flwing = get_flwing(name)
        self.attract = False


myPro = Profile()
pro = []
for i in range(len(myPro.flwing)):
    pro.append(Profile(mypro.flwing[i]))
    check = 0
while(True):
    for i in pro:
        milad(i)
        for i in range(len(Pro[check].flwing)):
            pro.append(Profile(Pro[check].flwing[i]))
