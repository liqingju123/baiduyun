# coding=utf-8
'''
Created on 2016年9月22日

@author: imac
'''

from itertools import *
from tqdm import tqdm
from time import sleep

str_num = ['0', '1', '2', '3']

# str_paixu = ''
str_len = len(str_num)

for inexd in range(str_len):
#     str_paixu=''
    str_paixu = str_num[inexd]  # 当前需要排序的
    j = 0;
    for j in range(inexd):  # 抽取之前的
        str_paixu = str_paixu + str_num[j];
        
    j = j + 1  
    for j in range(str_len):  # 抽取之后
        str_paixu = str_paixu + str_num[j];
        
#     print str_paixu
    
    
str_paixu = []   
for inexd in range(str_len):
    for inexd1 in range(str_len):
        str_paixu = []  
        for i in range(inexd1+1):
            if i != inexd:
                str_paixu.append(str_num[i])
#         print '====  '+str(str_paixu)
        str_paixu.append(str_num[inexd])
        k = inexd1-1
#         print k
        for k in range(str_len):
            if inexd1 != inexd:
                str_paixu.append(str_num[k])
     
     
#         print str_paixu
#     print '============='

#密码生成器
def psgen(x=4):
    iter = ['12abAB']
    for r in iter:
        for repeat in range(1,x+1):
            for ps in product(r,repeat=repeat):
                yield ''.join(ps)




def print_password():
    for ps in tqdm(psgen(6)):
        print ps

import sys,time

#自定义进度条

def progress_bar(bar_length, percent):
    hashes = '#' * int(percent / 100.0 * bar_length)
    spaces = ' ' * (bar_length - len(hashes))
    sys.stdout.write("\r我是进度条: 【%s 】%d%%" % (hashes + spaces, percent))
    sys.stdout.flush()

def progress_test(leng =101,bar_length=20):
    for percent in xrange(0, 101):
        progress_bar(bar_length, percent)
        time.sleep(1)
 
# progress_test()
# print


mapc ={'1':'11','2':'22','3':'33'}
pos2 = {value: key for (key, value) in mapc.items()}
# mapc2     for (value,key)  in mapc.items()

print pos2







    
