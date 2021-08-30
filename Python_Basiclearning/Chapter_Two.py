# Author: Cui De Cheng
# University: China University of Mining and Technology Beijing
# Position: Student
# Development time: 2021/8/6 17:50
# ----------------------------------------------------------------- #
# 二进制与字符编码
print(chr(0b100111001011000))
print(ord('乘'))

# 保留字
import keyword
print(keyword.kwlist)

# 变量
name = '玛丽亚'
print(name)
print('标识：', id(name))
print('类型：', type(name))
print('值：', name)

# 整数可以表示为二进制，八进制，十六进制
print("十进制：", 175)
print("二进制：", 0b110010)
print("八进制：", 0o176)
print("十六进制：", 0X1FBE)


# 浮点运算
n1 = 1.1
n2 = 2.2
print(n1+n2)
# 精确浮点运算
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))

# 字符串 ‘ 和 “ 只能在一行，”“” 可以多行
str1 = '字符串类型'
str2 = """字符串
类型"""

