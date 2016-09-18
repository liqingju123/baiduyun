# -*- coding: utf-8 -*- 

from selenium import webdriver
from time import sleep
#http://pythonscraping.com/pages/cookies/profile.php
browser = webdriver.Chrome(executable_path='/Users/imac/Downloads/chromedriver')
browser.get("http://pythonscraping.com/pages/cookies/login.html")
# browser.get("http://pythonscraping.com/pages/cookies/profile.php")
# sleep(10)
browser.add_cookie({'name':'username','value':'liqingju1111'})
browser.add_cookie({'name':'loggedin','value':'0'})
# browser.add_cookie({u'domain': u'pythonscraping.com', u'name': u'username', u'value': u'liqingju', u'path': u'/pages/cookies', u'httpOnly': False, u'secure': False})
# browser.add_cookie({u'domain': u'pythonscraping.com', u'name': u'loggedin', u'value': u'1', u'path': u'/pages/cookies', u'httpOnly': False, u'secure': False})

# sleep(5)
browser.find_element_by_name('username').clear()
browser.find_element_by_name('username').send_keys(u'liqingju')
# sleep(2)
browser.find_element_by_name('password').clear()
browser.find_element_by_name('password').send_keys(u'password')
# sleep(2)
sumble =browser.find_elements_by_tag_name('input')[2]
sumble.click()
# sleep(10)

print browser.get_cookie('loggedin')
