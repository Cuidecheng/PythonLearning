# Author: Cui De Cheng
# University: China University of Mining and Technology Beijing
# Position: Student
# Development time: 2021/8/10 10:21
# ----------------------------------------------------------------- #

s1 = 'abc'
s2 = 'abc'
print(s1 is s2)
s3 = 'abc%'
s4 = 'abc%'
print(s3 is s4)
a = 'abc'
b = 'ab' + 'c'
c = ''.join(['ab', 'c'])  # join方法的字符串拼接效率比‘+’的效率高
print(a is c)
print(c, type(c))

# 字符串查询操作
s = 'hello,hello'
print(s.index('lo'))  # 第一次出现lo的索引，没有则抛异常
print(s.find('lo'))   # 最后一次出现lo的索引，没有则抛异常
print(s.rindex('lo'))  # 第一次出现lo的索引，不会抛异常，输出-1
print(s.rfind('lo'))  # 最后一次出现lo的索引，不会抛异常，输出-1

# 大小写转换
s = 'hello,python'
a = s.upper()  # 转换后字符串id会改变
b = s.lower()  # 转换后字符串id会改变
s1 = 'HeLLo pYthon'
print(s1.swapcase())  # 大写转小写，小写转大写
print(s1.title())  # 每个单词首字母大写，其余小写

# 字符串对齐
s = 'hello,python'
print(s.center(20, '*'))
print(s.ljust(20, '*'))
print(s.rjust(20, '*'))
print(s.zfill(20))  # 有对齐，使用0填充
s1 = '-8910'
print(s1.zfill(20))
# 字符串分割
s = 'hello world python'
lst = s.split()
print(lst)
s1 = 'hello|world|python'
print(s1.split(sep='|'))  # 以|分割
print(s1.split(sep='|', maxsplit=1))  # 最多分1段
print(s.rsplit())  # 右分割
print(s1.rsplit('|'))
# 字符串判断
print('hello'.isidentifier())  # 是否是字符串
print('\t'.isspace())  # 是否由空白字符组成
print('abc'.isalpha())  # 是否全部由字母组成
print('123'.isdecimal())  # 是否全部由十进制的数字组成
print('123四Ⅱ'.isnumeric())  # 是否全部由数字组成
print('abc1'.isalnum())  # 是否全部由字母和数字组成
# 字符串的其他方法
s = 'hello, python'
print(s.replace('python', 'java'))
s1 = 'hello, python, python, python'
print(s1.replace('python', 'java', 2))

lst = ['hello', 'java', 'python']
print('|'.join(lst))
print(''.join(lst))

t = ('hello', 'java', 'python')
print(''.join(t))
print('*'.join('python'))

# 字符串比较
print('apple' > 'app')  # true
print('apple' > 'banana')  # false 相当于97>98 false
print(ord('a'), ord('b'))

#  == 与 is 的区别： == 比较的是value值，is 比较的是id值

s = 'hello,python'
print(s[:7])  # 字符串的切片
s1 = 'hello'
s2 = 'python'
print(s1 + '!' + s2)
# 切片[start:end:step]
print(s[-6::1])

# 格式化字符串
name = 'c'
age = 3
print('我叫%s,今年%d岁' % (name, age))
print(f'我叫{name},今年{age}岁')

print('%10d' % 99)  # 10表示的是宽度
print('hellohello')
print('%.3f' % 3.14159)  # .3表示的是精度
print('%10.3f' % 3.14159)
print('{}'.format(3.1415926))
print('{0:.3}'.format(3.1415926))  # .3表示的3位数
print('{:.3f}'.format(3.1415926))  # .3表示的3位小数
print('{:10.3f}'.format(3.1415926))

# 字符串的编码转换
s = '天涯共此时'
print(s.encode(encoding='GBK'))  # 在GBK这种编码格式中，一个中文占两个字节
print(s.encode(encoding='UTF-8'))  # 在UTF-8这种编码格式中，一个中文占三个字节

byte = s.encode(encoding='GBK')  # 编码
print(byte.decode(encoding='GBK'))  # 解码

byte = s.encode(encoding='UTF-8')  # 编码
print(byte.decode(encoding='UTF-8'))  # 解码


