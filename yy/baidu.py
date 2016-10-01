# encoding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path='/Users/imac/Downloads/chromedriver')
driver.get('http://www.baidu.com')
login_baidu =driver.find_element_by_class_name('lb')
print login_baidu.is_displayed()
login_baidu.click()
#driver.find_element_by_id('TANGRAM__PSP_10__unameLoginLink').click()
time.sleep(3)
driver.find_element_by_name('userName').send_keys('id')
driver.find_element_by_name('password').send_keys('passwd')
driver.find_element_by_id('TANGRAM__PSP_10__submit').click()
driver.find_element_by_css_selector('.user-name-top')
# webdriver.ActionChains(driver).move_to_element(user).perform() #移动鼠标到我的用户名
driver.find_element_by_css_selector('a.sep').click()
