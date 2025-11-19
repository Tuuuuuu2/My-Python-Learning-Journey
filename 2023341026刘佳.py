# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 20:30:51 2025

@author: Jia
"""

#针对题目一的回答
print('===你好，欢迎检测心理学灵力===')
print('\n===请如实输入你从2023年到2025年发表在SCI上的论文数！===\n')
y1 = int(input('请输入你在2023年在SCI上的论文发表数：'))
y2 = int(input('请输入你在2024年在SCI上的论文发表数：'))
y3 = int(input('请输入你在2025年在SCI上的论文发表数：'))
if y1 > 0 and y2 > 0 and y3 > 0: #检查每年发表数是否满足均大于0
    ymean = (y1+y2+y3)/3 #算平均数
    print('\n===恭喜通过检测！===\n您的年均发表篇数为'+str(ymean)+'篇')
    year_data = {2023:y1,2024:y2,2025:y3} #使用字典储存数据
    ymax = max(year_data,key=year_data.get) #使用内置函数
    ymin = min(year_data,key=year_data.get) #使用内置函数
    print(str(ymax)+"是你最有希望的一年！\n"+str(ymin)+'年你跌入谷底。')
    if ymean < 5: #用if条件+比较运算判断评级
        sentence = '小牛'
    elif ymean < 10:
        sentence = '牛'
    else:
        sentence = '牛中牛'
    print('=====你的评级为'+sentence+'=====')
else:
    print('对不起，您是废柴，无法进入灵力检测！')
print('\n免责声明：纯属娱乐，请勿当真！')



#针对题目二的回答
research_people = {
    "认知实验": ['刘小佳','小刘佳','刘人土土','刘佳小'],
    "情绪实验": ['小刘佳', '刘佳小', '刘人土土', '刘人土土'],
    "社会实验": ['刘小佳', '刘佳', '刘人土土', '刘小佳']
} #创建字典及内含列表来存储数据
#函数定义
def show_menu():
    '''显示主菜单'''
    print("\n===辛斐老师研究看管系统===")
    print("1.添加研究人员")
    print("2.查看所有实验人员")
    print("3.查找特定实验人员")
    print("4.退出系统")
def add_people():
    '''添加研究人员'''
    print("\n---添加研究人员---")
    experiment = input("请输入实验名称: ")
    people = input("请输入实验人员: ")
    if experiment in research_people: #检查实验是否在原本数据中
        research_people[experiment].append(people) #在的话直接添加人名
    else:
        research_people[experiment] = [people] #不在的话新创建添加
    print("成功添加数据:"+experiment+ '-'+str(people))
def show_all_people():
    '''显示所有研究实验及人员'''
    print("\n---所有研究实验人员---")
    for experiment, people in research_people.items(): #for循环遍历数据中的实验及人名
        print(experiment+':'+str(people))
def find_people():
    '''查找特定实验人员'''
    print("\n---查找研究实验人员---")
    experiment = input("请输入要查找的实验名称: ")
    if experiment in research_people: #判断实验名称是否存在
        print(experiment+'的主试情况:'+str(research_people[experiment]))
    else:
        print("未找到该实验的人员")
def main():
    '''统合几个功能'''
    print("欢迎使用辛斐老师研究看管系统！")
    while True:
        show_menu()
        choice = input("请选择功能(1-4): ")
        if choice == '1':
            add_people()
        elif choice == '2':
            show_all_people()
        elif choice == '3':
            find_people()
        elif choice == '4':
            print("感谢使用辛斐老师研究看管系统！")
            break #结束
        else:
            print("输入无效，请重新选择！")
main() #函数调用