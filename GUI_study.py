import tkinter as tk
from tkinter import ttk


root=tk.Tk()
root.title('护士量表系统(NOSIE)')
root.geometry('1636x2310+100+100')
#姓名
label_name=tk.Label(root,text='姓名',font=('宋体',15))
entry_name=tk.Entry(root,width=20,justify=tk.CENTER)
label_name.place(x=10,y=20)
entry_name.place(x=60,y=20)
#性别
label_sex=tk.Label(root,text='性别',font=('宋体',15))
entry_sex=tk.Entry(root,width=4,justify=tk.CENTER)
label_sex.place(x=200,y=20)
entry_sex.place(x=252,y=20)
#年龄
label_age=tk.Label(root,text='年龄',font=('宋体',15))
entry_age=tk.Entry(root,width=4)
label_age.place(x=290,y=20)
entry_age.place(x=340,y=20)
#病案号
label_patient_ID=tk.Label(root,text='病案号',font=('宋体',15))
entry_patient_ID=tk.Entry(root,width=20)
label_patient_ID.place(x=370,y=20)
entry_patient_ID.place(x=432,y=20)
#医院名称
label_hospital_name1=tk.Label(root,text='威海市立第三医院',font=('宋体',16))
label_hospital_name2=tk.Label(root,text='威海市精神卫生中心',font=('宋体',16))
label_hospital_name1.place(x=1636/2,y=100,anchor=tk.CENTER)
label_hospital_name2.place(x=1636/2,y=130,anchor=tk.CENTER)
#表名
label_sheet_name=tk.Label(root,text='护士用住院患者观察量表(NOSIE)',font=('宋体',20))
label_sheet_name.place(x=1636/2,y=180,anchor=tk.CENTER)
#双横线
# label_double_line=tk.Label(root,text='-----------------------------------------------------',font=100)
# label_double_line.place(x=1636/2,y=204,anchor=tk.CENTER)

separator=ttk.Separator(root,orient='horizontal')
separator.place(x=1636/2,y=204,width=400,anchor=tk.CENTER)
separator2=ttk.Separator(root,orient='horizontal')
separator2.place(x=1636/2,y=208,width=400,anchor=tk.CENTER)


#日期
#年
label_year=tk.Label(root,text='年',font=('宋体',12))
label_year.place(x=190,y=220)
entry_year=tk.Entry(root,width=12)
entry_year.place(x=100,y=220)
#月
label_month=tk.Label(root,text='月',font=('宋体',12))
label_month.place(x=290,y=220)
entry_nonth=tk.Entry(root,width=8)
entry_nonth.place(x=220,y=220)
#日
label_day=tk.Label(root,text='日',font=('宋体',12))
label_day.place(x=380,y=220)
entry_day=tk.Entry(root,width=8)
entry_day.place(x=320,y=220)
#表单号
label_sheet_ID=tk.Label(root,text='HLBD-059',font=('宋体',12))
label_sheet_ID.place(x=1636/2,y=220,anchor=tk.CENTER)

#创建frame对象，把下面的表格放在里面
frame=tk.Frame(root,width=1500,height=800)
frame.place(x=50,y=326)

#创建Canvas用于绘制表格1636x2310,并放置在frame中
canvas = tk.Canvas(frame, width=1500, height=800)
# canvas.pack(fill=tk.BOTH, expand=True)
# canvas.place(x=50,y=326)
canvas.place(x=0,y=0)

#在frame中增加下拉滚动条
h_scroll = ttk.Scrollbar(frame, orient=tk.HORIZONTAL, command=canvas.xview)
v_scroll = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
canvas.config(xscrollcommand=h_scroll.set, yscrollcommand=v_scroll.set)

# h_scroll.pack(side=tk.BOTTOM, fill=tk.X)
# v_scroll.pack(side=tk.RIGHT, fill=tk.Y)
# h_scroll.place(x=0,y=0)
v_scroll.place(x=1480,y=0)

# 使canvas成为滚动条操作的对象
canvas.config(scrollregion=canvas.bbox("all"))

# 绘制表格线
#绘制32条横线，注意，第一条线的坐标是如果是（0，0）的话不显示
for i in range(32):
     canvas.create_line(0,2+i*800/32,1480,2+i*800/32,fill="black")
#第一条竖线
canvas.create_line(2,0,2,800,fill='black')
#第二条竖线
canvas.create_line(300,0,300,800,fill='black')
#第三、四、五、六、七条竖线
for j in range(1,6):
    canvas.create_line(300+j*236,0,300+j*236,800)
#填充第一列内容：
#1、创建内容列表：
first_col_content=["项 目",
                    "1 肮脏",
                    "2 不耐烦",
                    "3 哭泣",
                    "4 对周围活动兴趣",
                    "5 不督促就一直坐",
                    "6 容易生气",
                    "7 听到不存在的声音",
                    "8 衣着保持整洁",
                    "9对人友好",
                    "10不如意便心烦",
                    "11 拒接做日常事务",
                    "12 易激动发牢骚",
                    "13 忘记事情",
                    "14 问而不答",
                    "15 对好笑的事发笑",
                    "16 进食狼藉",
                    "17 与人攀谈",
                    "18 自觉抑郁沮丧",
                    "19 谈论个人爱好",
                    "20 看到不存在的东西",
                    "21 提醒后才做事",
                    "22 不督促便一直睡着",
                    "23 自觉一无是处",
                    "24 不大遵守医院规则",
                    "25 难以完成简单任务",
                    "26 自言自语",
                    "27 行动缓慢",
                    "28 无故发笑",
                    "29 容易冒火",
                    "30 保持自身整洁"
                    ]
for i,item in enumerate(first_col_content):
    y=800/32/2+800/32*i
    canvas.create_text(60,y,text=item,anchor='w')

#将无、有时、常常、经常、一直是放在标题栏
four_content=['无','有时','常常','经常','一直是']
for i,item in enumerate(four_content):
    x=300 + 263/2+236*i
    canvas.create_text(x,800/32/2,text=item,anchor='center')




# #创建一个innerframe把选择按钮放在上面，让其在滑条滚动时，一起滚动
radio_frame=tk.Frame(canvas)
# canvas.create_window((0,0),window=radio_frame,anchor=tk.NW)
canvas.create_window((0, 0), window=radio_frame, anchor=tk.NW,
                     width=canvas.winfo_width()-h_scroll.winfo_reqwidth(),
                     height=canvas.winfo_height()-v_scroll.winfo_reqheight())  # 调整radio_frame大小适应Canvas的滚动区域

#将选择项分别加放在各个格里面
#选项菜单
#1、创建选项字典
option={"无":0,"有时":1,"常常":2,"经常":3,"一直是":4}
#2、创建一个选择函数
selected_value=tk.StringVar(value='无')
def radio_select():
    selected=selected_value.get()
    print(selected)

# for i,(lable,value) in enumerate(option.items()):
#     radio_bnt=tk.Radiobutton(radio_frame,text=lable,variable=selected_value,value=value)
#     # radio_bnt.place(x=418 + i * 236, y=800/32 + 800/32/2, anchor=tk.CENTER)
#     # radio_bnt.place(x=418 + i * 236, y=800/32 + 800/32/2, anchor=tk.CENTER)
#     radio_bnt.grid(row=1, column=i, padx=236, pady=800/32/2)

options_list = list(option.keys())

for row in range(32):  # 每一行
    for col in range(5):  # 每一列（五个选项）
        i = col  # 因为循环顺序是按选项来的，所以直接用col作为索引
        radio_bnt = tk.Radiobutton(radio_frame, text=options_list[i], variable=selected_value, value=option[options_list[i]], command=radio_select)
        radio_bnt.place(x=418 + col * 236, y=row * 800 / 32 + 800/32/2, anchor=tk.CENTER)
root.mainloop()
