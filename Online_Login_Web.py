#!/usr/bin/env python
# coding=utf-8
'''
Author: Shuangchi He / Yulv
Email: yulvchi@qq.com
github: https://github.com/Yulv-git
Date: 2021-02-08 11:36:34
Motto: Entities should not be multiplied unnecessarily.
LastEditors: Shuangchi He
LastEditTime: 2021-05-29 12:24:44
FilePath: /Campus_network_OM_WAL/Online_Login_Web.py
Description: 深大校园网  在线监测 & 网页版自动登录
1、修改用户名和密码，即可运行该脚本实现在线监测和校园网自动登录；
2、电脑上设置定时任务（每n秒执行该脚本），即可实现自动在线检测与登录；
3、设置上述两个步骤后，即可保证校园网不会掉线超过n秒（当然，需满足：处于开机状态、校园网没欠费、网线或无线连接好、校园网网页端没有变更）。
'''
import re
import requests
import datetime
import argparse


def Online_Check(test_web="https://www.baidu.com"):
    try:
        q = requests.get(test_web, timeout=5)
        STATUS = re.search(r'STATUS OK', q.text)
        if STATUS:
            print('\n【Check】 网络连接正常~')
            return True
        else:
            print('\n【Check】 网络连接异常！')
            return False
    except:
        print('\n【Check】 断网了 ......')
        return False


def Web_Login(args):
    if not Online_Check(test_web=args.test_web):
        data = {"DDDDD": args.user_name, "upass": args.password, "R1": 0, "R6": 0, "para": 00, "0MKKey": 123456}
        try:
            print("【Login】{} 设备网络离线，正在登录...\n".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            result = requests.post(args.Web_URL, data=data)
            print("【Login】{} 校园网登录成功~\n".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        except:
            print("【Login】{} 校园网登录失败，设备未连接网线或WIFI等！\n".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    else:
        print("【Login】{} 设备已在线, 无需再次登录校园网~\n".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))


if __name__ == "__main__":
    parse = argparse.ArgumentParser(description='Online_Login_Web')
    parse.add_argument('--test_web', default="https://www.baidu.com")
    parse.add_argument('--Web_URL', default="https://drcom.szu.edu.cn/a70.htm")
    parse.add_argument('--user_name', default=ahhhh)
    parse.add_argument('--password', default='23333')
    args = parse.parse_args()

    Web_Login(args)
