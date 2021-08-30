# Author: Cui De Cheng
# University: China University of Mining and Technology Beijing
# Position: Student
# Development time: 2021/8/17 15:55
# ================================================== #

import os


filename = 'student.txt'

def main():
    while True:
        menu()
        choice = int(input('请选择'))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input('您确定要退出系统吗？y/n\n')
                if answer == 'y' or answer == 'Y':
                    print('谢谢您的使用！！')
                    break  # 退出系统
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                modify()
            elif choice == 5:
                sort()
            elif choice == 6:
                total()
            elif choice == 7:
                show()

def menu():
    print("=======================学生信息管理系统===========================")
    print("--------------------------功能菜单------------------------------")
    print('\t\t\t\t1.录入学生信息')
    print('\t\t\t\t2.查找学生信息')
    print('\t\t\t\t3.删除学生信息')
    print('\t\t\t\t4.修改学生信息')
    print('\t\t\t\t5.排序')
    print('\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t0.退出')
    print("--------------------------------------------------------------")

def insert():
    student_list = []
    while True:
        s_id = input('请输入ID(如1001):')
        if not s_id:
            break
        name = input('请输入姓名:')
        if not name:
            break
        try:
            english = int(input('请输入英语成绩：'))
            python = int(input('请输入python成绩：'))
            java = int(input('请输入Java成绩：'))
        except:
            print('输入无效')
            continue
        # 将录入信息保存到字典中
        student = {'id': s_id, 'name': name, 'english': english, 'python': python, 'java': java}
        # 将学生信息添加到列表中
        student_list.append(student)
        answer = input('是否继续添加？y/n\n')
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break

    # 调用save()函数
    save(student_list)
    print('学生信息录入完毕！！！')

def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='UTF-8')
    except:
        stu_txt = open(filename, 'w', encoding='UTF-8')

    for item in lst:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()


    pass

def search():
    while True:
        get_info = []
        get_flag = 0
        if os.path.exists(filename):
            with open(filename, 'r', encoding='UTF-8') as file:
                stu_info = file.readlines()
        else:
            stu_info = []
        if stu_info:
            number = int(input('按ID查找请输入1，按姓名查询请输入2：'))
            d = {}
            if number == 1:
                stu_id = input('请输入学生的ID：')
                for item in stu_info:
                    print('item:', type(item))
                    print('eval(item)', type(eval(item)))
                    d = dict(eval(item))
                    if d['id'] == stu_id:
                        print('已找到该学生信息')
                        get_info.append(d)
                        get_flag = 1
                    else:
                        continue
                if get_flag != 1:
                    print('未找到该ID的学生信息')
                else:
                    print('info:', get_info)

                pass
            elif number == 2:
                stu_name = input('请输入学生的姓名')
                for item in stu_info:
                    d = dict(eval(item))
                    if d['name'] == stu_name:
                        print('已找到该学生信息')
                        get_info.append(d)
                        get_flag = 1
                    else:
                        continue
                if get_flag != 1:
                    print('未找到该ID的学生信息')
                else:
                    print('info:', get_info)

                pass
            else:
                print('不是以上两种方式，请重新输入！')
                continue

            answer = input('是否继续查找？y/n\n')
            if answer == 'y':
                continue
            else:
                print('查找功能已退出！')
                break
        else:
            print('无学生信息！')
            print('查找功能强制退出！')
            break



    pass

def delete():
    while True:
        student_id = input('请输入要删除的学生的ID：')
        if student_id != '':
            if os.path.exists(filename):
                with open(filename, 'r', encoding='UTF-8') as file:
                    student_old = file.readlines()
                    print('student_old 的类型是 ', type(student_old))
            else:
                student_old = []
            flag = False  # 标记是否删除的标志位
            if student_old:
                with open(filename, 'w', encoding='UTF-8') as wfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))  # 将字符串转成字典
                        if d['id'] != student_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print('id为{0}的学生信息已被删除'.format(student_id))
                    else:
                        print('没有找到id为{0}的学生信息'.format(student_id))
            else:
                print('无学生信息')
                break
            show()  # 删除后重新显示学生信息
            answer = input('是否继续删除？y/n\n')
            if answer == 'y':
                continue
            else:
                break

    pass

def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='UTF-8') as rfile:
            student_old = rfile.readlines()
        print('xinxi:', student_old)
    else:
        print('无学生信息')
        return
    student_id = input('请输入要修改的学生ID：')
    with open(filename, 'w', encoding='UTF-8') as wfile:
        for item in student_old:
            d = dict(eval(item))
            print('d', d)
            if d['id'] == student_id:
                print('已找到学生信息')
                while True:
                    try:
                        d['name'] = input('请输入学生姓名')
                        d['english'] = int(input('请输入英语成绩:'))
                        d['python'] = int(input('请输入python成绩：'))
                        d['java'] = int(input('请输入Java成绩：'))
                    except:
                        print('您的输入有误请重新输入')
                    else:
                        break
                wfile.write(str(d) + '\n')
                print('修改成功')
            else:
                wfile.write(str(d) + '\n')
                print('未找到该ID的学生的信息')
        answer = input("是否继续修改其他学生信息？y/n\n")
        if answer == 'y':
            modify()

    pass

def sort():

    pass

def total():

    pass

def show():

    pass

if __name__ == '__main__':
    main()





















