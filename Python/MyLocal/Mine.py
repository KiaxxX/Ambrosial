# -*- coding: utf8 -*-
# python >=3.8

import requests, time, re, json, random, dingtalkchatbot.chatbot as dd


now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


## 钉钉机器人推送
def push_dd(sckey, desp=""):
    """
    推送消息到钉钉机器人
    """
    if sckey == '':
        print(f"[{now}][WORN]未提供sckey，不进行推送！")
    else:
        server_url = sckey
        param = desp

        ding = dd.DingtalkChatbot(server_url)
        response = ding.send_text(msg=param, at_dingtalk_ids=['8ke-8x04ndda6', 'lkh017'])

        if response['errcode'] == 0:
            print(f"[{now}][SUCCESS]推送成功。")
        else:
            print(f"[{now}][ERROR]推送失败：{response['errcode']}({response['errmsg']})")

if __name__ == "__main__":
    sckey = 'https://oapi.dingtalk.com/robot/send?access_token=c68c392bd46d79145ffb52ef2e589f75120d42a41260de354a540080eeb8fcbe'
    push_dd(sckey, '[INFO] 陈新平， 起床了！她还没醒呢吧')
    print(sckey.find('123'))
    print(sckey.find('s'))