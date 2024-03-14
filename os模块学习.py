# #把目录中所有的py文件打印出来
# import os
# path=os.getcwd()
# dirs=os.listdir(path)
# for file in dirs:
#     # a,b=os.path.splitext(file)
#     # # print(b)
#     # if b=='.py':
#     if file.endswith('py'):
#         print(file)


#walk函数
# import os
# path=os.getcwd()
# dir=os.walk(path)
# for dirpath,dirnames,filenames in dir:
#     '''print(dirpath)
#     print(dirnames)
#     print(filenames)
#     print('-------------------------------------------------')'''
#     for dirn in dirnames:
#         print(os.path.join(dirpath,dirn))
#     for filenm in filenames:
#         print(os.path.join(dirpath,filenm))
#
#
#     for item in file:
#         d=dict(eval(item))

'''向文件中输出：奋斗成就更好的你'''
# with open('宣言.txt','w') as file:
#     word='奋斗成就更好的你!'
#     file.write(word)

# '''figue converse'''
# num=int(input('Please input a number:'))
# print('The binary format of this number is:',bin(num))
# print('The Octal format of this number is:%s'%oct(num))
# print('The Hexacdecimal format of this number is:{}'.format(hex(num)))


# '''velify zhifubao password'''
# pw='369852'
# while True:
#     inptpw=input('Please input the correct passord:\n')
#     if str.isdigit(inptpw):
#         if inptpw==pw:
#             print("The password you have input is correct,success!")
#             break
#         else:
#             print("The password you have input is not correct!please input the right password!")
#     else:
#         print("The password should input digit!please input the right password!")


import pyautogui
# img=r'C:\Users\Administrator\Desktop\img1.png'
# location=pyautogui.locateCenterOnScreen(img,confidence=0.9)
# print(location)
#
# x,y=pyautogui.position()
# print(x,y)
# # pyautogui.click(x,y)
# x,y=100,200
# a=pyautogui.onScreen(x,y)
# width,height=pyautogui.size()
# print(width,height)
# import random
# import pandas as pd
#
# while True:
#     a = random.randint(0, 1024)
#     b = random.randint(0, 1024)
#     pyautogui.moveTo(a,b,duration=1)
#     if a==100:
#         break
a=r'C:\Users\Administrator\Desktop\pythonStudy\waterRPA\img2.png'
b=r'C:\Users\Administrator\Desktop\pythonStudy\waterRPA\google.png'
position=pyautogui.locateCenterOnScreen(a,confidence=0.7)
position2=pyautogui.locateCenterOnScreen(b,confidence=0.7)
print(position,position2)
pyautogui.moveTo(position)
pyautogui.click(x=181, y=727,clicks=2,interval=0.2,duration=2)
# pyautogui.click(position2)
