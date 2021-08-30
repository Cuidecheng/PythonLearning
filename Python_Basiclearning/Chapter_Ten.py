# Author: Cui De Cheng
# University: China University of Mining and Technology Beijing
# Position: Student
# Development time: 2021/8/12 22:19
# ----------------------------------------------------------------- #

def calc(a, b):
    c = a+b
    return c
# 位置传参
result = calc(10, 20)
print(result)
# 关键字传参
result1 = calc(b=10, a=20)  # 传参给名字相同的参数
print(result1)

def fun(arg1, arg2):
    print('arg1', arg1)
    print('arg2', arg2)
    arg1 = 100
    arg2.append(10)
    print('arg1', arg1)
    print('arg2', arg2)

n1 = 11
n2 = [20, 30, 40]
fun(n1, n2)
print('n1', n1)
print('n2', n2)
'''在参数调用过程中，进行参数的传递
如果是不可变对象，在函数体的修改不会影响实参的值，arg1的修改为100，不会影响n1的值
如果是可变对象，在函数体的修改会影响到实参的值，arg2的修改.append(10)，会影响到n2的值
'''

def fun2(num):
    odd = []
    even = []
    for i in num:
        if i % 2:
            odd.append(i)
        else:
            even.append(i)
    return odd, even

lst = [10, 29, 34, 23, 44, 53, 55]
print(fun2(lst))
'''
函数的返回值
(1)如果函数没有返回值(函数执行完毕后，不需要给调用出提供数据) return可与i省略不写
(2)函数的返回值，如果是一个，直接返回类型
(3)函数的返回值，如果是多个，返回的结果为元组
'''


# 个数可变的位置参数
# @可能无法事先确定传递的位置实参的个数时，使用可变的位置参数
# @结果为一个元组
# @该参数只能是一个
def fun4(*args):
    print(args)

fun4(10)
fun4(10, 30)
fun4(10, 30, 50)

# 个数可变的关键字形参
# @无法事先确定传递的关键字实参的个数时，使用可变的关键字形参
# @输出的结果为字典
# @该参数只能有一个
def fun5(**args):
    print(args)

fun5(a=10)
fun5(a=20, b=30, c=50)

# 在一个函数的定义过程中，既有个数可变的关键字形参，又有个数可变的位置形参，要求：个数可变的位置形参放在个数可变的关键字形参之前

def fun6(a, b, c):
    print('a = ', a)
    print('b = ', b)
    print('c = ', c)

# 函数的调用
fun6(20, 30, 40)  # 位置传参
lst = [20, 30, 40]
fun6(*lst)  # 将列表中的每一个元素都转换为位置实参传入
fun6(a=10, b=20, c=30)  # 关键字实参
dic = {'a': 111, 'b': 222, 'c': 333}
fun6(**dic)  # 将字典中的键值对都转换为关键字实参传入

# 要求c,d只能使用关键字实参传递
def fun7(a, b, *, c, d):  # 从*之后的参数，在函数调用时，只能才用关键字参数传递
    print('a = ', a)
    print('b = ', b)
    print('c = ', c)
    print('d = ', d)
fun7(10, 20, c=30, d=40)

# 函数定义时的形参的顺序问题
def fun8(a, b, *, c, d, **args):
    pass
def fun9(*args, **args2):
    pass
def fum10(a, b, *args, **args2):
    pass

# 变量的作用域
def fun11(a, b):
    c = a+b  # c为局部变量
    print(c)
f = 10
def fun12():
    print(f)  # f为全局变量

def fun13():
    global age  # 全局变量
    age = 20
    print(age)

fun13()
print(age)

# 递归函数
# 阶乘
def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n-1)

print(fac(6))

