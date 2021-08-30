# Author: Cui De Cheng
# University: China University of Mining and Technology Beijing
# Position: Student
# Development time: 2021/8/16 17:41
# ----------------------------------------------------------------- #

# 调用自己编写的模块
import Diycalc
print(Diycalc.add(10, 20))

from Diycalc import add
print(add(20, 30))

import Diycalc2
print(add(50, 60))


# 常用的内容模块
import sys
import time
import urllib.request

print(sys.getsizeof(23))  # 所占长度
print(sys.getsizeof(True))
print(sys.getsizeof(False))

print(time.time())
print(time.localtime(time.time()))
# print(urllib.request.urlopen('http://www.baidu.com').read())  # 读取百度网站的数据信息，爬虫时使用

import schedule

def job():
    print('哈哈哈---')

schedule.every(3).seconds.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)


