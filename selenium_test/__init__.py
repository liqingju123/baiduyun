# -*- coding: utf-8 -*- 

from selenium import webdriver
from time import sleep
import os  

# profile_dir=u"/Users/imac/Library/Application Support/Google/Chrome/Default"    # 对应你的chrome的用户数据存放路径  
# chrome_options=webdriver.ChromeOptions()  
# chrome_options.add_argument("user-data-dir="+os.path.abspath(profile_dir))  



def add_cookie_whit_url(browser):
    browser.add_cookie({u'domain':u'.pan.baidu.com', u'name':u'Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0', u'value':u'1474186213', u'path':u'/', u'httpOnly':False, u'secure':False})
    browser.add_cookie({u'domain':u'.pan.baidu.com', u'secure':False, u'value':u'1474186205', u'expiry':1505722213, u'path':u'/', u'httpOnly':False, u'name':u'Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0'})
    browser.add_cookie({u'domain':u'pan.baidu.com', u'name':u'Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0', u'value':u'1474179499', u'path':u'/', u'httpOnly':False, u'secure':False})
    browser.add_cookie({u'domain':u'pan.baidu.com', u'name':u'Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0', u'value':u'1473829166,1473836628,1474179499', u'path':u'/', u'httpOnly':False, u'secure':False})
    browser.add_cookie({u'domain':u'pan.baidu.com', u'name':u'SCRC', u'value':u'356d5eaf427ab31e76a3e7558fe3ddb6', u'path':u'/', u'httpOnly':False, u'secure':False})
    browser.add_cookie({u'domain':u'pan.baidu.com', u'name':u'BIDUPSID', u'value':u'50D69C72F98A07624EC5DA75711F2E0B', u'path':u'/', u'httpOnly':False, u'secure':False})
    browser.add_cookie({u'domain':u'pan.baidu.com', u'name':u'STOKEN', u'value':u'5f781b7212b57c63f3298d9634d7466bfac91b7e61db68e5f4e4c26f887c9f01', u'path':u'/', u'httpOnly':False, u'secure':False})
    browser.add_cookie({u'domain':u'pan.baidu.com', u'name':u'MCITY', u'value':u'-%3A', u'path':u'/', u'httpOnly':False, u'secure':False})
    browser.add_cookie({u'domain':u'pan.baidu.com', u'name':u'secu', u'value':u'1', u'path':u'/', u'httpOnly':False, u'secure':False})
    browser.add_cookie({u'domain':u'pan.baidu.com', u'name':u'bdshare_firstime', u'value':u'1459921997754', u'path':u'/', u'httpOnly':False, u'secure':False})
    browser.add_cookie({u'domain':u'pan.baidu.com', u'name':u'PANPSC', u'value':u'17131005371540458033%3AENVL4Mn25ShKeos2hhgdg%2Bn90oj%2BY%2FIs34lshz6CkL%2BRhxLNg7Jg8452N20FG1l54huX1R9Xo1kwwo4y0uRbvSy6%2B%2BBAeydjc8JXjRU%2FLbf%2F5yY%2B2yl0OZpZfis7W4JlvY40bMUDX1j76jyG3uDkPYshZ7OchQK1KQDQpg%2B6XCV%2BSJWX9%2F9F%2FIkt7vMgzc%2BT', u'path':u'/', u'httpOnly':False, u'secure':False})
    browser.add_cookie({u'domain':u'pan.baidu.com', u'name':u'PSTM', u'value':u'1459843710', u'path':u'/', u'httpOnly':False, u'secure':False})
    browser.add_cookie({u'domain':u'pan.baidu.com', u'name':u'BAIDUID', u'value':u'50D69C72F98A07624EC5DA75711F2E0B:FG=1', u'path':u'/', u'httpOnly':False, u'secure':False})
    browser.add_cookie({u'domain':u'pan.baidu.com', u'name':u'PANWEB', u'value':u'1', u'path':u'/', u'httpOnly':False, u'secure':False})
    browser.add_cookie({u'domain':u'.baidu.com', u'secure':False, u'value':u'01142853DF397F5E25E7A399F121C531:FG=1', u'expiry':1505722204.506553, u'path':u'/', u'httpOnly':False, u'name':u'BAIDUID'})
    browser.add_cookie({u'domain':u'.baidu.com', u'secure':False, u'value':u'15%3A3', u'expiry':1475050213, u'path':u'/', u'httpOnly':False, u'name':u'cflag'})
    browser.add_cookie({u'domain':u'pan.baidu.com', u'name':u'BDUSS', u'value':u'mE4My05LU9RYkdFbzJxRkx5ZjBkRmNwQ0JkcmFNa1FhbTl-Q2d4S29WRm9OMUJYQVFBQUFBJCQAAAAAAAAAAAEAAAApejtW1eLKx8uttcTLrTEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGiqKFdoqihXU', u'path':u'/', u'httpOnly':False, u'secure':False})
    browser.add_cookie({u'domain':u'.pan.baidu.com', u'secure':False, u'value':u'1', u'expiry':1505722204.50578, u'path':u'/', u'httpOnly':False, u'name':u'PANWEB'})
    browser.add_cookie({u'domain':u'pan.baidu.com', u'name':u'cflag', u'value':u'15%3A3', u'path':u'/', u'httpOnly':False, u'secure':False})

def add_cookie(browser):
    browser.add_cookie({'name':'BAIDUID', 'value':'50D69C72F98A07624EC5DA75711F2E0B:FG=1'})
    browser.add_cookie({'name':'BIDUPSID', 'value':'50D69C72F98A07624EC5DA75711F2E0B'})
    browser.add_cookie({'name':'PSTM', 'value':'1459843710'})
    browser.add_cookie({'name':'PANWEB', 'value':'1'})
    browser.add_cookie({'name':'bdshare_firstime', 'value':'1459921997754'})
    browser.add_cookie({'name':'BDUSS', 'value':'mE4My05LU9RYkdFbzJxRkx5ZjBkRmNwQ0JkcmFNa1FhbTl-Q2d4S29WRm9OMUJYQVFBQUFBJCQAAAAAAAAAAAEAAAApejtW1eLKx8uttcTLrTEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGiqKFdoqihXU'})
    browser.add_cookie({'name':'secu', 'value':'1'})
    browser.add_cookie({'name':'MCITY', 'value':'-%3A'})
    browser.add_cookie({'name':'STOKEN', 'value':'5f781b7212b57c63f3298d9634d7466bfac91b7e61db68e5f4e4c26f887c9f01'})
    browser.add_cookie({'name':'SCRC', 'value':'356d5eaf427ab31e76a3e7558fe3ddb6'})
    browser.add_cookie({'name':'Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0', 'value':'1473829166,1473836628,1474179499'})
    browser.add_cookie({'name':'Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0', 'value':'1474179499'})
    browser.add_cookie({'name':'PANPSC', 'value':'17131005371540458033%3AENVL4Mn25ShKeos2hhgdg%2Bn90oj%2BY%2FIs34lshz6CkL%2BRhxLNg7Jg8452N20FG1l54huX1R9Xo1kwwo4y0uRbvSy6%2B%2BBAeydjc8JXjRU%2FLbf%2F5yY%2B2yl0OZpZfis7W4JlvY40bMUDX1j76jyG3uDkPYshZ7OchQK1KQDQpg%2B6XCV%2BSJWX9%2F9F%2FIkt7vMgzc%2BT'})
    browser.add_cookie({'name':'cflag', 'value':'15%3A3'})

browser = webdriver.Chrome(executable_path='/Users/imac/Downloads/chromedriver')

browser.get("https://pan.baidu.com/disk/home#list/path=%2F")
# cookie_baidu ={'Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0':'1473846759','Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0':'1473846759','BDUSS':'HpKQ1hjY1MzeXNPY1Z5ajY0M0VsT3Q3SklhZWJYdzUwVjh5RkdjMUMwdnBxZ0JZQVFBQUFBJCQAAAAAAAAAAAEAAAApejtW1eLKx8uttcTLrTEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOkd2VfpHdlXN'}
add_cookie_whit_url(browser)



# add_cookie(browser)

# sleep(5)
# base_text =browser.find_element_by_id('u').get_attribute('innerHTML')
# print  base_text +'===== '
# sleep(100)
# browser.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("18610530592")
# browser.find_element_by_id("TANGRAM__PSP_4__password").send_keys("likaibo150")
# browser.find_element_by_id("TANGRAM__PSP_4__submit").click()
sleep(4)
# browser.find_element_by_class_name('dlg-mbox-close').click()
 
browser.get("https://pan.baidu.com/disk/home#list/path=%2F")
browser.find_element_by_class_name('dlg-mbox-close').click()

print browser.get_cookies()
# browser.save_screenshot('/Users/imac/Downloads/screen.png')
sleep(2)
browser.find_element_by_id("h5Input1").send_keys(u'/Users/imac/Downloads/测试脚本.txt')
# browser.find_element_by_id('dialog-close').click()


