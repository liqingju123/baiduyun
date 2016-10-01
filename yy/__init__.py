# -*- coding: utf-8 -*- 

from selenium import webdriver
from time import sleep
import os  
import unittest



def login(browser):
    browser.find_element_by_id('nav-login').click() # ActionChains(browser).move_by_offset(x1,0).perform()
    browser.switch_to_frame('udbsdk_frm_normal')
    sleep(5)
    list_input = browser.find_element_by_xpath('//*[@id="m_commonLogin"]/div[1]/span/input')
    list_input.send_keys('li973683374')
    list_input = browser.find_element_by_xpath('//*[@id="m_commonLogin"]/div[2]/span/input')
    list_input.send_keys('likaibo150+')
    browser.find_element_by_xpath('//*[@id="m_commonLogin"]/div[5]/a[1]').click()

def add_cookie_whit_url(browser):
    browser.add_cookie({u'domain': u'.huya.com', u'name': u'_yasids', u'value': u'__rootsid%3DC73E9383FA4000013DD714506B8086D0', u'path': u'/', u'httpOnly': False, u'secure': False})
    browser.add_cookie({u'domain': u'.huya.com', u'name': u'__yaoldyyuid', u'value': u'119571972', u'path': u'/', u'httpOnly': False, u'secure': False})
    browser.add_cookie({u'domain': u'.huya.com', u'secure': False, u'value': u'0.7906110432612152', u'expiry': 1535810331, u'path': u'/', u'httpOnly': False, u'name': u'__yamid_tt1'})
    browser.add_cookie({u'domain': u'.huya.com', u'secure': False, u'value': u'AEDSBVBqAAJgAGI6Qct7wDsKgJ17mH71ARYStFt5IFWqRV0eUad1LONZQ_hCmHQ2AsVP7VbynzInrCy0hW_FQR-Bhy6uf1PlSg1sC8F2kL07ZOd3Ra-ilcGgH7EfuVkg9iULkLQc5atWGA==', u'expiry': 1475935142.490963, u'path': u'/', u'httpOnly': False, u'name': u'udb_c'})
    browser.add_cookie({u'domain': u'.huya.com', u'secure': False, u'value': u'1475330331', u'expiry': 1506866349, u'path': u'/', u'httpOnly': False, u'name': u'Hm_lvt_51700b6c722f5bb4cf39906a596ea41f'})
    browser.add_cookie({u'domain': u'.huya.com', u'secure': False, u'value': u'03a304a19ec5f5c0fbafcad75f2019cfb8e510e9ad5c2a8c0201876eb816febd22bfab7f0505d7ca2b5461a1299f9538', u'expiry': 1475935142.489887, u'path': u'/', u'httpOnly': False, u'name': u'udb_n'})
    browser.add_cookie( {u'domain': u'.huya.com', u'secure': False, u'value': u'CwBsaTk3MzY4MzM3NCTB71cCcwBCxiWTO58bmJ5_IWdVAvbghXXwclrzSGAmkL46G1k4otzvqRnZqpPpUqHwCjPEi5AdVowb9r4oRYInK4QM6b3bjH6buXFi8p1fiKirRQvkU2-a5M22X5KRM-GaBcSPb89782lctFjJGOixyiZuKjESMbRtAAAAAAMAAAAAAAAADQA0Mi4yMzguMTYzLjUzBAA1MjE2', u'expiry': 1475935142.487544, u'path': u'/', u'httpOnly': False, u'name': u'udb_l'})
    browser.add_cookie({u'domain': u'.huya.com', u'secure': False, u'value': u'C73E937F5D600001CE3519B118921468', u'expiry': 1538402331, u'path': u'/', u'httpOnly': False, u'name': u'__yamid_new'})
    browser.add_cookie({u'domain': u'.huya.com', u'secure': False, u'value': u'li973683374', u'expiry': 1475935142.483877, u'path': u'/', u'httpOnly': False, u'name': u'username'})
    browser.add_cookie({u'domain': u'.huya.com', u'name': u'ya_eid', u'value': u'navi/sign', u'path': u'/', u'httpOnly': False, u'secure': False})
    browser.add_cookie( {u'domain': u'.www.huya.com', u'secure': False, u'value': u'', u'expiry': 1475331232, u'path': u'/', u'httpOnly': False, u'name': u'udboauthtmptokensec'})
    browser.add_cookie({u'domain': u'www.huya.com', u'name': u'hdjs_session_id', u'value': u'0.5422785144519808', u'path': u'/', u'httpOnly': False, u'secure': False})
    browser.add_cookie( {u'domain': u'.huya.com', u'secure': False, u'value': u'0.1877937606288005', u'expiry': 4628930331, u'path': u'/', u'httpOnly': False, u'name': u'hd_newui'})
    browser.add_cookie({u'domain': u'.huya.com', u'secure': False, u'value': u'BDDF74965419D79E4D1EA7DE76D8682DF69A0244', u'expiry': 1475935142.485905, u'path': u'/', u'httpOnly': False, u'name': u'osinfo'})
    browser.add_cookie( {u'domain': u'www.huya.com', u'secure': False, u'value': u'4df59aff-8023-44cc-8f90-35db77e4b987', u'expiry': 1535810326, u'path': u'/', u'httpOnly': False, u'name': u'__FEQUALITY__UUID'})
    browser.add_cookie( {u'domain': u'.huya.com', u'name': u'Hm_lpvt_51700b6c722f5bb4cf39906a596ea41f', u'value': u'1475330350', u'path': u'/', u'httpOnly': False, u'secure': False})
    browser.add_cookie({u'domain': u'.huya.com', u'secure': False, u'value': u'1', u'expiry': 1475935140.605429, u'path': u'/', u'httpOnly': False, u'name': u'h_pr'})
    browser.add_cookie( {u'domain': u'.huya.com', u'secure': False, u'value': u'1475330345', u'expiry': 1475935145.312852, u'path': u'/', u'httpOnly': False, u'name': u'h_unt'})
    browser.add_cookie({u'domain': u'www.huya.com', u'name': u'hdjs_session_time', u'value': u'1475330349796', u'path': u'/', u'httpOnly': False, u'secure': False})   
    browser.add_cookie( {u'domain': u'.huya.com', u'secure': False, u'value': u'4A9272185158A993A3E2F8721648427B0D6DE592B5FFC89EF589A901A46422819E63B2430588862233E226FC5C01E86325B1C1DD2E0A81D56526AE757544D0B269ECF4B9F29B12FDA5FB035D832F9318744B7EFA0CDD64242E4BCC5FB4038DAEC572F197D505377D6703FEBBA8F137E257E4EEC199EC81DF85826D4406422A076009D630A6D9CA91625543286091F398445CAB22B1BF7A3994013FBD2995D04C2AE72171F3CB36B2A7D39EEEE2C5AC9B2F4AD0C6B59ED3F768BE916880560D7C41E57E0A85E92AA6A4EAB893688C98446D314CB161C97DF8E4A8F17F99D3F73FB5DF893D52DEC8CB9FB76F48AB6F7FAF74004626C30D27B6B88C4CD50F4E7DDA7293DFF8671C835BF86693103E8697E551BA7CCD72C6CF06A60595AAA51ADD95C6788FEBBF720FF906A0E9A13E521947D18C7700D98C14EF4FEF03921E7F8DFB', u'expiry': 1475935142.492479, u'path': u'/', u'httpOnly': False, u'name': u'udb_oar'}) 
    browser.add_cookie({u'domain': u'.huya.com', u'secure': False, u'value': u'7793b1db1ec1ef578e136c0a6d0a6bb5', u'expiry': 1477922335, u'path': u'/', u'httpOnly': False, u'name': u'guid'}) 
    browser.add_cookie({u'domain': u'.huya.com', u'secure': False, u'value': u'0.09185829595408634', u'expiry': 1535810331, u'path': u'/', u'httpOnly': False, u'name': u'hiido_ui'}) 
    browser.add_cookie( {u'domain': u'.www.huya.com', u'secure': False, u'value': u'856301c6195a1274ec4a6d1df51050e1e6c9d97fe19618ab5d694e3d110a4e23203fedb04519f8dd6fa83ddef37d61ad2e1b82fb568bc8e5a96327380962f688', u'expiry': 1475331232, u'path': u'/', u'httpOnly': False, u'name': u'udboauthtmptoken'}) 
    browser.add_cookie({u'domain': u'.huya.com', u'secure': False, u'value': u'D10A38C72BF4D71CD6F0C6316E545BB522778C4D', u'expiry': 1475935142.484813, u'path': u'/', u'httpOnly': False, u'name': u'password'}) 
    browser.add_cookie({u'domain': u'www.huya.com', u'name': u'PHPSESSID', u'value': u'mb1r3at4t9m5lcridpas94kcu6', u'path': u'/', u'httpOnly': False, u'secure': False}) 
    browser.add_cookie( {u'domain': u'.huya.com', u'secure': False, u'value': u'0.6', u'expiry': 1475416748, u'path': u'/', u'httpOnly': False, u'name': u'SoundValue'}) 
    browser.add_cookie( {u'domain': u'.huya.com', u'secure': False, u'value': u'119571972', u'expiry': 1475935142.482773, u'path': u'/', u'httpOnly': False, u'name': u'yyuid'})
    browser.add_cookie( {u'domain': u'.huya.com', u'name': u'__yasmid', u'value': u'0.7906110432612152', u'path': u'/', u'httpOnly': False, u'secure': False})

browser = webdriver.Chrome(executable_path='/Users/imac/Downloads/chromedriver')

browser.get("http://www.huya.com/408655394")
# add_cookie(browser)
sleep(4)
# login(browser)
add_cookie_whit_url(browser)
sleep(2)
browser.get("http://www.huya.com/408655394")
browser.switch_to.default_content()
while True:
    browser.find_element_by_id('pub_msg_input').send_keys(u'深水炸弹')
#     sleep(1)
    browser.find_element_by_id('msg_send_bt').click()
# browser.get("http://www.huya.com/408655394")



# print '===='+str(len(list_input))


# alert_div.find_element_by_class_name('E_acct').send_keys('liqingju')


# browser.find_element_by_class_name('E_acct').send_keys('likaibo150+')
# alert_div =browser.find_element_by_class_name('login')
# browser.find_element_by_class_name('close').click()
# list_input =alert_div.find_elements_by_class_name('placeholder')
# print '======'+str(len(list_input))


# browser.find_element_by_xpath('//*[@id="m_commonLogin"]/div[2]/span/input').send_keys('likaibo150+')
# sleep(4)
# browser.find_element_by_class_name('E_login').click()
print browser.get_cookies()



