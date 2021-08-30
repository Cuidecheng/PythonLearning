# Author: Cui De Cheng
# University: China University of Mining and Technology Beijing
# Position: Student
# Development time: 2021/8/6 11:44
# ----------------------------------------------------------------- #

# 打印输出
print("hello world")

# 将数据输出到文件中
fp = open("E:/Graduate/PythonProject/Python_Basiclearning/text.txt", 'a+') # a+: 如果文件不存在就创建，存在就在文件内容的后面继续追加
print("hello world", file=fp)
fp.close()

# 转义字符
print("hello\nword")
# 原字符，不以往字符串中的转义字符起作用，就使用元字符，则在字符串之前加上r/R
print(r'hello\nworld')  # 最后一个字符不能是反斜线

