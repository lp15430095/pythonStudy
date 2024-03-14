# decode:uft-8

# print("hellow world!")
#
# #注释
# """这也是注释，是多行注释"""
# # a=10
# b=-10
# c=1.2
# print(type(a))
# print(type(b))
# print(type(c))
# str1="I"
# str2="love"
# str3="you"
# str=str1+str2+str3
# print(str)
# ##########数组
# a=3
# b=5
# c=a>b
# # print(c)
#
# dic=[1,2,3,a,b,c]
# dic.append("d")
# dic.insert(3,10)
# # del dic[1]
#
# # ############输入输出
# # name=input("请输入你的名字：")
# # print("你输入的名字是："+name)

####用占位符输出
# name=""
# age=""
# sex=""

# name=input("请输入姓名：")
# age=input("请输入年龄：")
# sex=input("请输入性别：")
# str="""
#     name  :%s
#     age   :%s
#     sex   :%s
#     """%(name,age,sex)
# print(str)

#####流程控制，if-else
#
# a=2
# b=3
# if a>=b:
#     print("a>=b")
# else:
#     print("a<b")

########成绩测试
"""
A:100-90
B:90-80
C:80-70
D:70-
"""
# #提示用户输入成绩
# score=input("请输入您本次考试成绩：")
# if 90<float(score)<=100:
#     print("你成绩等级为A")
# elif 80<float(score)<=90:
#     print("你成绩等级为B")
# elif 70<float(score)<=80:
#     print("你成绩等级为C")
# else:
#     print("你成绩等级为D")



# #打印0到100的偶数
# i=0
# for i in range(100):
#     print(2*i)




# ###内存地址
# name1=1
# name2=name1
# name1=2
# print(name1)
# print(name2)
#
# ###列表
# list1=[1,2,3,4]
# print(list1.)

###字典

# dict1={"name":"lin","age":18,"sex":"男"}
# dict1["work"]='engner'
# print(dict1)
# #####hash算法
#
# print(hash("我爱你"))

#####编码和解码encode/decode
# import binascii
# str="I love you"
# str1=str.encode('gbk')
# str2=str1.decode('gbk')
# print(str1)
# print(str2)

# print(help('with'))


# ####function
# def prt():
#     print('This is my first function!')
# def coculat(a,b):
#     return a+b
# prt()
# t=coculat(1,3)
# print(t)

##高阶函数
# #1、求余函数
# def remain(a,b):
#     r=a%b
#     return r
# def sum(x,y,f):
#     return f(x,y)
# t=sum(100,200,remain)
# print(t)
# print(hex(100))

# a=int(input('请输入a\n'))
# b=int(input('请输入b\n'))
#
# # t=a if a>b else b
# # print(f'您要的结果是{t}')
# print(f'您要的结果是{a if a>b else b}')
#
# # print('您要的结果是'+str(a if a>b else b))
# # 2
# # print(r'http:\\www.baidu.com')

#计算1-100的偶数和
# sum=0
# for item in range(2,101,2):
#     sum+=item
# print(sum)
#



#求100-999之间的水仙花数

# for i in range(100,1000):
#     j=str(i)
#     if int(j[0])**3+int(j[1])**3+int(j[2])**3==i:
#         print(i)


# #列表生成式
# lis=[i**2 for i in range(10)]
# lis1=[i*j for i,j in range(10)]
# print(lis1)


###字符串
#
# str='abcdea'
# n_str=str.replace()
# print(n_str)



####异常处理，被动掉坑
try:
    a=int(input("请输入第一个整数："))
    b=int(input("请输入第二个整数："))
    c=a/b
    print('两个数的和是：',c)
except ValueError:
    print('只能输入数字')
    print('程序退出')
except ZeroDivisionError:
    print('0不能当除数！')
    print('程序退出')
except BaseException as e:
    print('输入有问题请联系信息管理员')
finally:
    print('谢谢使用')