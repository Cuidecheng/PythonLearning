# Author: Cui De Cheng
# University: China University of Mining and Technology Beijing
# Position: Student
# Development time: 2021/8/14 15:48
# ----------------------------------------------------------------- #

# bug异常的捕获
# try...except结构
try:
    a = int(input('输入第一个整数：'))
    b = int(input('输入第二个整数：'))
    result = a/b
    print('结果为：', result)
except ZeroDivisionError:
    print('除数不能为零')
except ValueError:
    print('只能输入字符串')
print('程序结束')

# try...except...else 结构
try:
    a = int(input('输入第一个整数：'))
    b = int(input('输入第二个整数：'))
    result = a/b
except BaseException as e:
    print('出错了')
else:
    print('结果为：', result)

# try...except...else...finally 结构
try:
    a = int(input('输入第一个整数：'))
    b = int(input('输入第二个整数：'))
    result = a/b
except BaseException as e:  # 可以吸收所有异常
    print('出错了')
else:
    print('结果为：', result)
finally:  # 执行完try excep/else后，总会执行finally
    print('Thank you')

''' 常见异常类型
ZeroDivisionError   除零
IndexError  序列中没有此索引
KeyError    映射中没有这个键
NameError   未声明/初始化对象
SyntaxError     Python语法错误
ValueError      传入无效的参数
'''

# traceback 模块的使用
'''
import traceback
try:
    print('----------')
    print(1/0)
except:
    traceback.print_exc()
'''

