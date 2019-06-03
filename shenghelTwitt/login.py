from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pickle

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
        
pickle.dump(value, open('cookie.st','wb'))
