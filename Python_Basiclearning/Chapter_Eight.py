# Author: Cui De Cheng
# University: China University of Mining and Technology Beijing
# Position: Student
# Development time: 2021/8/9 21:08
# ----------------------------------------------------------------- #

# 可变序列： 列表，字典
# 不可变序列： 字符串， 元组
# 元组创建
t = ('python', 'world', 98)
t1 = tuple(('python', 'world', 98))
t2 = ('python', )
print(type(t), type(t1), type(t2))
t3 = ()
t4 = tuple()
# 元组的遍历
for item in t:
    print(item)

# 集合：没有value的字典
# 创建
s = {2, 3, 5, 4, 5, 4, 8, 8, 7}
print(s)  # 集合中的元素不允许重复
s1 = set(range(5))
s2 = set([2, 3, 5, 4, 5])
s3 = set((2, 3, 5, 4, 5))
s4 = set('python')
print(s4)  # 无序不重复序列
# 空
s5 = set()
# 操作
s.add(80)  # 添加一个
s.update({22, 50, 13})  # 至少添加一个
s.remove(13)  # 集合内没有该元素会报错
s.discard(25)  # 集合没有也不会报错
s.pop()  # 删除任意一个， 不能添加参数

# 是否是子集
s1 = {10, 20, 30, 40, 50, 60}
s2 = {10, 20, 30, 40}
s3 = {10, 20, 90}
print(s2.issubset(s1))  # s2是s1的子集 -》 True
print(s3.issubset(s1))  # 不是 -》 False
print(s1.issuperset(s2))  # s1是s2的超集
print(s2.isdisjoint(s3))  # 是否没有交集 -》False
print(s1.intersection(s2))  # 输出交集
print(s1 & s2)  # 输出交集
print(s1.union(s2))  # 输出并集
print(s1 | s2)  # 输出并集
print(s1.difference(s2))  # 输出差集
print(s1 - s2)  # 输出差集
print(s1.symmetric_difference(s2))  # 输出对称差集（异或）
print(s1 ^ s2)  # 输出异或集合
# 集合生成式
set1 = {i*i for i in range(9)}
print(set1)












