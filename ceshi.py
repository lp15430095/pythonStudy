import tkinter as tk
root =tk.Tk()
root.geometry('500x300+200+200')
label_name=tk.Label(root,text='用户名：',font=('隶书',20),fg='red',bg='green')
label_name.place(x=10,y=10)
label_pass=tk.Label(root,text='密  码：',font=('隶书',20),fg='red',bg='green')
label_pass.place(x=10,y=50)
disport={'admin':'abc','linpeng':'123456'}
var_name=tk.StringVar()
var_pass=tk.StringVar()
def login():
    if var_name.get() in disport.keys():
        for key,value in disport.items():
            if var_name.get()==key and var_pass==value:
                break



entry_name=tk.Entry(root,textvariable=var_name,font=('隶书',20),width=10)
entry_name.place(x=133,y=10)
entry_pass=tk.Entry(root,textvariable=var_pass,font=('隶书',20),width=10,show='*')
entry_pass.place(x=133,y=50)
print(var_name.get(),var_pass.get())
label_confirm=tk.Label(root,text='确定',font=('隶书',20),fg='red')
label_confirm.place(x=100,y=100)
label_concel=tk.Label(root,text='取消',font=('隶书',20),fg='red')
label_concel.place(x=200,y=100)
root.mainloop()