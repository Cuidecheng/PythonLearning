# Author: Cui De Cheng
# University: China University of Mining and Technology Beijing
# Position: Student
# Development time: 2021/8/14 17:25
# ----------------------------------------------------------------- #

class Student:  # 首字母大写，其余小写
    native_place = '山东'  # 直接写在类里面的变量，成为类属性

    def __init__(self, name, age):
        self.name = name  # 成为实体属性，进行了一个赋值操作，将局部变量的name的值赋给实体属性
        self.age = age

    # 实例方法
    def eat(self):
        print('学生在吃饭。')

    # 静态方法
    @staticmethod
    def method():
        print('使用staticmethod进行修饰，所以是静态方法')

    # 类方法
    @classmethod
    def cm(cls):
        print('使用classmethod进行修饰，所以是类方法')

    pass

# 创建Student类的对象
stu1 = Student('张三', 20)
stu1.eat()  # 对象名.方法名()
print(stu1.name, stu1.age)

Student.eat(stu1)  # 类名.方法名(实例对象)   // 与stu1.eat()的功能相同

# 类属性的使用方法
print(Student.native_place)

stu1 = Student('张三', 20)
stu2 = Student('李四', 25)
print(stu1.native_place)
print(stu2.native_place)
Student.native_place = '天津'
print(stu1.native_place)
print(stu2.native_place)

# 类方法的使用方式
Student.cm()

# 静态方法的使用方式
Student.method()
print('--------------------------------------------')


# 动态绑定属性和方法

class Student1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat1(self):
        print(self.name + '在吃饭')
    pass

stu3 = Student1('张三', 20)
stu4 = Student1('李四', 25)

# 动态绑定属性
stu3.gender = '女'  # 单独为stu3绑定属性
print(stu3.name, stu3.age, stu3.gender)
print(stu4.name, stu4.age)  # stu4中没有

# 动态绑定方法
stu3.eat1()
stu4.eat1()
def show():
    print('定义在类之外的函数')

stu3.show = show  # 为stu3绑定新的函数
stu3.show()  # 绑定后输出  # stu4中没有











