# class Student:
#     def __init__(self,name,sex):#初始化方法，为新建的对象括中的初始化用的 如stu1('张三’，‘女’)
#         self.name=name
#         self.sex=sex
#     nativeplace='RiZhao'#在类中的变量叫”类属性“
#     def eat(self):
#         print(self.name+'正在吃饭')#类方法
#     @staticmethod
#     def mechod():#静态方法
#         #print('类'+self.name+'正在吃饭')
#         print('这是静态方法')
#     @classmethod#类方法
#     def Class_mechod(cls):
#         print('这是类方法')
#
# #实例化一个对象
# stu1=Student('张三','男')
# stu2=Student('李四','女')
# #验证实例方法
# stu1.eat()
# stu2.eat()
# #验证类方法
# Student.Class_mechod()
# #验证静态方法
# Student.mechod()
# #类属性
# stu1.nativeplace='威海'
# print(stu1.nativeplace)
# print(stu2.nativeplace)
#



"""类的封装"""
# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age
#     def show(self):
#         print(self.name,self.__age)
# stu=Student('zhangsan',20)
# stu.show()
# print(stu.name)


# class Car:
#     def __init__(self,brand,long,wide,high):
#         self.brand=brand
#         self.long=long
#         self.wide=wide
#         self.high=high
#     def show(self):
#         print(f'The brand of car is {self.brand},the long of car is {self.long},\
# the wide of the car is {self.wide} \nthe high of the car is {self.high}')
#
# car=Car('宝马','400cm','150cm','140cm')
# car.show()


#
# class Pig:
#     def __init__(self,sex,color):
#         self.sex=sex
#         self.color=color
#     def show(self):
#         print(f'This is a {self.sex} pig,its color is {self.color},I like pork!')
# pig=Pig('male','black')
# pig.show()


'''类的继承'''
#建一个交亲
class Person(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print('这是父类打印出的东西')
# #建一个学生子类
# class Student(Person):
#     def __init__(self,name,age,stu_no):
#         super().__init__(name,age)
#         self.stu_no=stu_no
# #建一个老师类
# class Teacher(Person):
#     def __init__(self,name,age,tea_no):
#         super().__init__(name,age)
#         self.tea_no=tea_no
# #建一个学生和老师的实例
# stu=Student('zhangsan','10',1001)
# tea=Teacher('lisi','30','2002')
# stu.show()
# tea.show()


# a=10
# b=20
# c=a.__add__(b)
# print(c)
# print(dir(a))


# ###text
#
# class Test:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def prt(self):
#         print(f'姓名是{self.name},年龄是{self.age}')
#
# test=Test('zhangsan',19)
# test.prt()



### with 文件管理器
with open(r'C:\Users\Administrator\Desktop\abc.docx','rb') as scr_file:
    with open(r'C:\Users\Administrator\Desktop\abcd.docx','wb') as target_file:
        target_file.write(scr_file.read())
