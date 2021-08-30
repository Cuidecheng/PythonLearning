# Author: Cui De Cheng
# University: China University of Mining and Technology Beijing
# Position: Student
# Development time: 2021/8/9 20:47
# ----------------------------------------------------------------- #

# 字典
student1 = {'name': 'cdc', 'age': 23}
student2 = dict(name='cdc', age=23)
# 获取字典的元素
print(student2['name'])
print(student2.get('age'))
print(student2.get('city'), 'tj')  # tj是在查找的键值不存在时输出的默认值
student2['city'] = 'TJ'  # 新增
print(student2)
del student2['age']  # 删除操作
print(student2)
print(student2.keys())
print(student2.values())
print(student2.items())
s_key = student2.keys()
print(list(s_key))  # 将获取的键转换成列表
# 遍历
for item in student2:
    print(item, student2[item])

items = ['name', 'age', 'city']
prices = ['c', 10, 'BJ']
d = {item: price for item, price in zip(items, prices)}
print(d)


