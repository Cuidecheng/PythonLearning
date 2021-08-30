# Author: Cui De Cheng
# University: China University of Mining and Technology Beijing
# Position: Student
# Development time: 2021/8/6 18:18
# ----------------------------------------------------------------- #

# input功能
a = input("输入加数：")
b = input("输入被加数：")
print(type(a), type(b)) # 输入的类型为str
print(int(a)+int(b))

# 赋值运算符
a = 20
b, c, d = 30, 40, 50
# 变量交换
e, f = 30, 40
e, f = f, e

# 比较运算符
a = 10
b = 10
print(a == b)  # True，a与b的value 相等
print(a is b)  # True, a与b的id 也相等

lst1 = [11, 22, 33, 44]
lst2 = [11, 22, 33, 44]
print(lst1 == lst2)  # value --> True
print(lst1 is lst2)  # id --> False

print(a is not b)  # False
print(lst1 is not lst2)  # True

# bool运算符
a, b = 1, 2
print(a == 1 and b < 2)  # False    True and False --> False
print(a == 1 or b < 2)  # True    True and False --> True
s = 'helloworld'
print('w' in s)  # True
print('k' not in s)  # True1

# 移位运算符
print(4 << 1)
print(4 >> 2)

# 运算符优先级:  算术运算 》 位运算 》 比较运算 》 布尔运算 》 赋值运算

# 条件if语句
score = input('请输入一个成绩')
score = int(score)
# 方式一：
if score <= 100 and score >= 60:
    print('A')
elif score <= 590 and score >= 0:
    print('B')
else:
    print('error')
# 方式二：
if 60 <= score <= 100:
    print('A')
elif 0 <= score <= 59:
    print('B')
else:
    print('error')

# 条件表达式：
num_a = int(input('输入第一个整数'))
num_b = int(input('输入第二个整数'))
# if语句判断，为真，执行左边，为假执行右边
print(str(num_a) + '>=' + str(num_b) if num_a >= num_b else str(num_a) + '<' + str(num_b))

# range()函数的三种创建方式
a = range(10)  # 0-9
a = range(2, 10)  # 2-9
a = range(1, 10, 2)  # 1-9 步长为2

# for
# for i in range(10)
# for _ in range(5)  # 如果自变量用不到可以使用'_'
# 输出100-999的水仙花数
for item in range(100, 1000):
    ge = item % 10
    shi = item // 10 % 10
    bai = item // 100
    if ge**3+shi**3+bai**3 == item:
        print(item)

# break
# continue
# else
for item in range(3):
    pwd = input("请输入密码：")
    if pwd == '8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
else:
    print('对不起密码三次均错误')

# 输出3行4列矩阵
for i in range(1, 4):
    for j in range(1, 5):
        print('*', end='\t')
    print()  # 换行
# 打印直角三角形
for i in range(1, 10):
    for j in range(1, i+1):
        print(i, '*', j, '=', i*j, end='\t')
    print()



