# -*- encoding: utf-8 -*-
'''
@File    :   网络调试.py
@Time    :   2022/09/18 15:20:41
@Author  :   随便写
@Email   :   66666@163.com
'''

# here put the import lib
import tkinter as tk
from tkinter import ttk
import socket
import idTest

#ip 地址初始化
# mac ip
ip = socket.gethostbyname_ex(socket.gethostname())[2]


root = tk.Tk()
root.title('调试工具')
root.geometry('650x500+100+100')




# 左边布局
left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT, anchor=tk.N,padx=5,pady=5)

# 左边布局 网络设置
net_frame = tk.LabelFrame(left_frame,text='网络设置',padx=15,pady=5)
net_frame.pack()

tk.Label(net_frame,text='(1)IP地址').pack(anchor=tk.W)
socket_host = ttk.Combobox(net_frame)
socket_host['values'] = ip
socket_host.current(1)
socket_host.pack()


tk.Label(net_frame,text='(2)线程 假的现在做不了多线程').pack(anchor=tk.W)
thread_num = ttk.Combobox(net_frame)
thread_num['values'] = [1,5,10,20,50,100]
thread_num.current(0)
thread_num.pack()

'''
tk.Label(net_frame,text='(3)输入框').pack(anchor=tk.W)
entry_port = ttk.Entry(net_frame)
entry_port.pack(fill=tk.X)
'''

def pri():
    n_ip =  socket_host.get()
    t_num = thread_num.get()
    text_pad.insert("end", f"开始寻找！！ IP：{n_ip}，线程：{t_num} \n")
    idTest.main(text_pad,n_ip,t_num)



# 按钮
button_frame = tk.Frame(net_frame)
button_frame.pack()
open_btn = tk.Button(button_frame,text='开始',command=pri)
close_btn = tk.Button(button_frame,text='结束')
open_btn.pack(side=tk.LEFT)
close_btn.pack(side=tk.RIGHT)



# 右边布局
right_frame = tk.Frame(root)
right_frame.pack(side=tk.TOP,padx=5,pady=5)

info_frame = tk.Frame(right_frame)
info_frame.pack()
tk.Label(info_frame,text='日志').pack(anchor=tk.W)

text_pad = tk.Text(info_frame,width=52)
text_pad.pack(side=tk.LEFT,fill=tk.X)


tk.Label(right_frame,text='获取到的账号').pack(anchor=tk.W)
send_frame = tk.Frame(right_frame)
send_frame.pack()




send_area = tk.Text(send_frame)
send_area.pack(side=tk.LEFT,fill=tk.X)
send_area.insert("end", '不想做了')
root.mainloop()


