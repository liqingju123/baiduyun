#coding=utf-8

'''
Created on 2016年9月22日

@author: liqingju
'''
import smtplib
from email.mime.text import MIMEText 
from email.header import Header
from time import sleep

username ='likaiboo@126.com'
password ='13728488966'
receiver = '656021898@qq.com'

# username111 ='likaiboo111@126.com'

#发送邮件主题
subject = '我自己的测试服务发送' #发送邮箱服务器
smtpserver = 'smtp.126.com' #发送邮箱用户/密码
#中文需参数‘utf-8’,单字节字符不需要
msg = MIMEText('我是李庆举','text','utf-8')
msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = 'likaiboo@126.com'    
msg['To'] = receiver  
smtp = smtplib.SMTP() 
smtp.connect('smtp.126.com') 
smtp.login(username, password) 
for index in range(600):
    if index % 10 ==0:
        smtp = smtplib.SMTP() 
        smtp.connect('smtp.126.com') 
        smtp.login(username, password) 
        sleep(10)
        print '登录'
    else:
        smtp.sendmail(username, receiver, msg.as_string()) 
    print '发送一个成功'
smtp.quit()
print '发送完成'




