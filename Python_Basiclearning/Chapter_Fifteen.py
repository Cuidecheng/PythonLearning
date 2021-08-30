# Author: Cui De Cheng
# University: China University of Mining and Technology Beijing
# Position: Student
# Development time: 2021/8/16 19:55
# ----------------------------------------------------------------- #

file = open('text.txt', 'r')
print(file.readline())  # 读取一行
file.close()

file1 = open('b.txt', 'w')
file1.write('hello world')
file1.close()

file2 = open('b.txt', 'a')
file2.write('hello world')
file2.close()

src_file = open('cat.png', 'rb')  # 读取二进制文件
target_file = open('copycat.png', 'wb')  # 复制一个新的图片(写二进制文件)
target_file.write(src_file.read())
target_file.close()
src_file.close()

file3 = open('text.txt', 'r')
print(file3.read(2))  # 读取两个字符
file3.close()

file4 = open('text.txt', 'r')
print('@@@@@')
print(file4.readlines())  # 以一行为单位放入到列表中
file4.close()
print('@@@@@')

file5 = open('text.txt', 'a')
lst = ['python', 'hello', 'world']
file5.writelines(lst)  # 将列表追加到txt文件中
file5.close()

file6 = open('text.txt', 'r')
file6.seek(2)  # 跳过两个字节
print(file6.read())
print(file6.tell())  # 输出文件内最后一个字符的位置
file6.close()

file7 = open('text.txt', 'a')
file7.write('good')
file7.flush()  # 把缓冲区的内容写入文件，但不关闭文件
file7.write('day')
file7.close()

# with语句 (上下文管理器)

class MyContentMgr(object):
    def __enter__(self):
        print('enter方法被调用执行了')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit方法被调用执行了')

    def show1(self):
        print('show被调用执行了')
    pass

with MyContentMgr() as file8:  # 相当于file = MyContentMgr()
    file8.show1()  # 不管该方法执行时是否产生异常，都会执行exit()操作

# 文件的复制
with open('cat.png', 'rb') as src_file1:
    with open('copycat2.png', 'wb') as target_file2:
        target_file2.write(src_file1.read())

print('-----------------')

import os  # os模块是Python内置的与操作系统功能和文件系统相关的模块
# os.system('calc.exe')  # 打开系统中的计算器

# 直接调用可执行文件
# os.startfile('D:\\Software\\Work\\TIM\\Bin\\TIM.exe')  # 打开tim

print(os.getcwd())  # 得到当前路径
print(os.listdir('../Python_Basiclearning'))  # 返回指定路径下的文件和目录信息

# os.mkdir('newdir')  # 创建目录
# os.makedirs('A/B/C')  # 创建多级目录
# os.rmdir()  # 删除目录
# os.removedirs()  # 删除多级目录
# os.chdir('')  # 将path设置为当前工作目录

# os.path模块操作目录相关函数
import os.path

print(os.path.abspath('Chapter_Fifteen.py'))  # 用于获取文件或目录的绝对路径
print(os.path.exists('Chapter_Ten.py'), os.path.exists('Chapter_Fifteen22.py'))  # True  False 用于判断路径或目录是否存在
print(os.path.join('E:\\Graduate\\PythonProject', 'Python_Basiclearning'))  # 路径的拼接操作
print(os.path.split('E:\\Graduate\\PythonProject\\Python_Basiclearning\\Chapter_Fifteen.py'))  # 将路径和文件的名字进行拆分
print(os.path.splitext('Chapter_Fifteen.py'))  # 将文件的名字和后缀名进行拆分
print(os.path.basename('E:\\Graduate\\PythonProject\\Python_Basiclearning\\Chapter_Fifteen.py'))  # 从一个目录中提取文件名
print(os.path.dirname('E:\\Graduate\\PythonProject\\Python_Basiclearning\\Chapter_Fifteen.py'))  # 从一个路径中提取文件路径，不包括文件名
print(os.path.isdir('E:\\Graduate\\PythonProject\\Python_Basiclearning'))  # 判断是否为路径

print('----------------')

# 列出指定目录下的所有py文件
import os
path = os.getcwd()
lst = os.listdir(path)
for filename in lst:
    if filename.endswith('.py'):
        print(filename)

print('---------------------')

# 列出多级目录下的文件
import os
path1 = os.getcwd()
lst_files = os.walk(path)






