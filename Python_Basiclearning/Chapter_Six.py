# Author: Cui De Cheng
# University: China University of Mining and Technology Beijing
# Position: Student
# Development time: 2021/8/9 17:49
# ----------------------------------------------------------------- #
# 列表
'''
列表特点：
列表元素按顺序有序排列
索引映射唯一数据
列表可以储存重复数据
任意数据类型混存
根据需要动态分配和回收内存
example：见jupyter notebook
'''
lst = ['hello', 'world', 98, 'hello']
print(lst.index('hello'))
print(lst.index('hello', 1, 4))  # 从索引范围内查找内容
lst.append(80)
lst2 = [90, 'python']
lst.extend(lst2)  # 不能写成lst=extend(90, 'python')
print(lst)
# 列表生成式
lst = [i for i in range(1, 10)]
print(lst)





