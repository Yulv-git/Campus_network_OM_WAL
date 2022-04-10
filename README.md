<!--
 * @Author: Shuangchi He / Yulv
 * @Email: yulvchi@qq.com
 * @Date: 2021-02-08 11:36:34
 * @Motto: Entities should not be multiplied unnecessarily.
 * @LastEditors: Shuangchi He
 * @LastEditTime: 2022-04-10 23:32:14
 * @FilePath: /Campus_network_OM_WAL/README.md
 * @Description: Campus network online monitoring and web version automatic login.
-->

<h1><center> Campus_network_OM_WAL </h1></center>

    Campus network online monitoring and web version automatic login.

---

- [1. SZU校园网，Python登录](#1-szu校园网python登录)
  - [1.1. Windows定时任务，实现在线监测与自动登录](#11-windows定时任务实现在线监测与自动登录)
  - [1.2. Linux定时任务，实现在线监测与自动登录](#12-linux定时任务实现在线监测与自动登录)
- [2. SZU校园网，JavaScript登录](#2-szu校园网javascript登录)

---

# 1. SZU校园网，Python登录

## 1.1. Windows定时任务，实现在线监测与自动登录

设置[Windows定时运行Python脚本](https://blog.csdn.net/qq_37828488/article/details/100049421)，即可实现在Windows开机状态下的自动在线监测和校园网登录。

## 1.2. Linux定时任务，实现在线监测与自动登录

- 在个人用户目录下，运行```crontab -e```命令定时任务配置文档，并进行编辑。
- 输入```*/1 * * * * python3 ./Python/Online_Login_Web.py >> ./auto_login.log 2>&1```，并保存退出。即可实现在Linux开机状态下的自动在线监测和校园网登录。

# 2. SZU校园网，JavaScript登录

在浏览器开发者模式下，使用[JavaScript](./JavaScript/Online_Login_Web.js)进行校园网登录。
