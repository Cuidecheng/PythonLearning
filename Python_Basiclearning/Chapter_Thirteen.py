# Author: Cui De Cheng
# University: China University of Mining and Technology Beijing
# Position: Student
# Development time: 2021/8/15 17:41
# Development time: 2021/8/15 17:41
# ----------------------------------------------------------------- #


class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 年龄不希望在类的外部被使用，所以加了__

    def show(self):
        print(self.name, self.__age)
pass

stu = Student('张三', 20)
stu.show()  # 可以访问到age

print(stu.name)
# print(stu.__age)  # 不能访问age,报错
# 获取方法
# print(stu._Student__age)  # 流氓访问法。。。 一般不访问

print('---------------------------')

# 继承
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(self.name, self.age)
pass

class Student2(Person):
    def __init__(self, name, age, stu_no):
        super().__init__(name, age)
        self.stu_no = stu_no

    def info(self):  # 方法重写
        super(Student2, self).info()
        print(self.stu_no)
pass

class Teacher(Person):
    def __init__(self, name, age, year):
        super().__init__(name, age)
        self.year = year

    def info(self):  # 方法重写
        super(Teacher, self).info()
        print(self.year)
pass

stu = Student2('张三', 20, '1001')
teacher = Teacher('李四', 34, 10)

stu.info()
teacher.info()

# object类
class Student3:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return 'my name is {0}, {1} years old'.format(self.name, self.age)
pass

stu1 = Student3('张三', 21)
print(dir(stu1))
print(stu1)
print(type(stu1))

# 多态
class Animals:
    def eat(self):
        print('动物要吃东西')
pass

class Dog(Animals):
    def eat(self):
        print('狗吃骨头')
pass

class Cat(Animals):
    def eat(self):
        print('猫吃鱼')
pass

class Person2(object):
    def eat(self):
        print('人吃五谷杂粮')

def fun(obj):
    obj.eat()

fun(Cat())
fun(Dog())
fun(Animals())
fun(Person2())


# 特殊属性
class A:
    pass
class B:
    pass
class C(A, B):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    pass

x = C('jack', 22)
print(x.__dict__)  # 实例对象的属性字典
print(C.__dict__)
print(x.__class__)  #<class '__main__.C'> 输出了对象所属的类
print(C.__bases__)  # C类的父类类型的元组
print(C.__base__)
print(C.__mro__)  # 查看类的层次结构
print(A.__subclasses__())  # 查看A类的子类都哪些(列表)

# 特殊方法
# __add__()
a = 10
b = 30
c = a + b
d = a.__add__(b)
print(c, d)

class Student4:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        return self.name + other.name

    def __len__(self):
        return len(self.name)
    pass

stu3 = Student4('张三')
stu4 = Student4('李四')
s = stu3 + stu4  # 必须重写__add__后才能使用
stu_len = len(stu3)  # 必须重写__len__后才能使用
print(s, stu_len)
print('----------------------------')


# __new__() 与 __init__()
class Person3(object):
    def __new__(cls, *args, **kwargs):
        print('__new__()被调用执行了，cls的ID值为{0}'.format(id(cls)))
        obj = super().__new__(cls)
        print('创建的对象的ID值为{0}'.format(id(obj)))
        return obj

    def __init__(self, name, age):
        print('__init__()被调用执行了，cls的ID值为{0}'.format(id(self)))
        self.name = name
        self.age = age

print('object这个类对象的ID为：{0}'.format(id(object)))
print('Person这个类对象的ID为：{0}'.format(id(Person3)))

# 创建Person3类的实例对象
p1 = Person3('张三', 20)
print('p1这个Person类的实例对象的ID：{0}'.format(id(p1)))

print('-------------')

# 类对象的赋值操作
class CPU:
    pass
class Disk:
    pass
class Computer:
    def __init__(self, cpu, ying):
        self.cpu = cpu
        self.ying = ying
    pass

cpu1 = CPU()
cpu2 = cpu1
print(cpu1)
print(cpu2)

# 类的浅拷贝
disk = Disk()
computer = Computer(cpu1, disk)

import copy
computer2 = copy.copy(computer)  # 拷贝时，对象包含的子对象内容不拷贝
print(computer, computer.cpu, computer.ying)
print(computer2, computer2.cpu, computer2.ying)

print('------------------')

# 类的深拷贝
computer3 = copy.deepcopy(computer)  # 深拷贝，拷贝对象中包含的子对象
print(computer, computer.cpu, computer.ying)
print(computer3, computer3.cpu, computer3.ying)








