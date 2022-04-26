# -*- coding: utf8 -*-
# python >=3.8
import base64
import hashlib
import hmac
import json
import random
import re
import time
import urllib

import dingtalkchatbot.chatbot as dd
import requests

now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
headers = {"User-Agent": "Dalvik/2.1.0 (Linux; U; Android 10; MI 11 pro MIUI/21.8.18)"}


# 获取登录code
def get_code(location):
    code_pattern = re.compile("(?<=access=).*?(?=&)")
    code = code_pattern.findall(location)[0]
    return code


# 登录
def login(user, pwd):
    headers = {
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "User-Agent": "MiFit/5.2.0 (iPhone; iOS 14.5.1; Scale/2.00)"}
    regist_url = "https://api-user.huami.com/registrations/+86" + user + "/tokens"
    regist_data = {
        "client_id": "HuaMi",
        "password": f"{pwd}",
        "redirect_uri": "https://s3-us-west-2.amazonaws.com/hm-registration/successsignin.html",
        "token": "access"
    }
    regist_res = requests.post(regist_url, data=regist_data, headers=headers, allow_redirects=False)
    try:
        location = regist_res.headers["Location"]
        code = get_code(location)
    except:
        return 0, 0
    # print("access_code获取成功!")
    # print(code)

    # dev = random.choice(["", "__IDFA2__", "__IDFA__", "00000000-0000-0000-0000-000000000000", "default"])  # 随机取地址
    login_url = "https://account.huami.com/v2/client/login"
    login_data = {
        "app_name": "com.xiaomi.hm.health",
        "app_version": "5.2.0",
        "code": f"{code}",
        "country_code": "CN",
        "device_id": "default",
        "device_model": "phone",
        "grant_type": "access_token",
        "third_name": "huami_phone"
    }
    login_res = requests.post(login_url, data=login_data, headers=headers).json()
    login_token = login_res["token_info"]["login_token"]
    userid = login_res["token_info"]["user_id"]

    return login_token, userid


# 主函数
def main(user, pwd, name, step):
    user = str(user)
    pwd = str(pwd)
    name = name
    step = str(step)

    if user == "" or pwd == "":
        print(f"[{now}][ERROR]用户名或密码不能为空!")
        return f"[{now}][ERROR] Username and Password Must Be Not Empty!"

    login_token, userid = login(user, pwd)
    if login_token == 0:
        print(f"[{now}][ERROR]登陆失败!")
        return f"[{now}][ERROR]Can't Login!"

    app_token = get_app_token(login_token)

    today = time.strftime("%F")

    data_json = "%5B%7B%22data_hr%22%3A%22%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F9L%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F" \
                "%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2FVv%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F" \
                "%5C%2F0v%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F9e%5C%2F%5C%2F%5C%2F%5C%2F" \
                "%5C%2F0n%5C%2Fa%5C%2F%5C%2F%5C%2FS%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F" \
                "%5C%2F0b%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F1FK%5C%2F%5C%2F%5C%2F%5C%2F%5C" \
                "%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2FR%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F" \
                "%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F9PTFFpaf9L%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F" \
                "%5C%2F%5C%2F%5C%2F%5C%2F%5C%2FR%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C" \
                "%2F0j%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F9K%5C%2F%5C%2F%5C%2F%5C%2F%5C" \
                "%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2FOv%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C" \
                "%2F%5C%2F%5C%2Fzf%5C%2F%5C%2F%5C%2F86%5C%2Fzr%5C%2FOv88%5C%2Fzf%5C%2FPf%5C%2F%5C%2F%5C%2F0v%5C%2FS" \
                "%5C%2F8%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2FSf%5C%2F%5C%2F" \
                "%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2Fz3%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F0r%5C" \
                "%2FOv%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2FS%5C%2F9L%5C%2Fzb%5C%2FSf9K%5C%2F0v%5C%2FRf9H%5C%2Fzj%5C" \
                "%2FSf9K%5C%2F0%5C%2F%5C%2FN%5C%2F%5C%2F%5C%2F%5C%2F0D%5C%2FSf83%5C%2Fzr%5C%2FPf9M%5C%2F0v%5C%2FOv9e" \
                "%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2FS%5C%2F%5C%2F%5C%2F%5C%2F%5C" \
                "%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2Fzv%5C%2F%5C%2Fz7%5C%2FO%5C%2F83%5C%2Fzv%5C%2FN%5C%2F83" \
                "%5C%2Fzr%5C%2FN%5C%2F86%5C%2Fz%5C%2F%5C%2FNv83%5C%2Fzn%5C%2FXv84%5C%2Fzr%5C%2FPP84%5C%2Fzj%5C%2FN%5C" \
                "%2F9e%5C%2Fzr%5C%2FN%5C%2F89%5C%2F03%5C%2FP%5C%2F89%5C%2Fz3%5C%2FQ%5C%2F9N%5C%2F0v%5C%2FTv9C%5C%2F0H" \
                "%5C%2FOf9D%5C%2Fzz%5C%2FOf88%5C%2Fz%5C%2F%5C%2FPP9A%5C%2Fzr%5C%2FN%5C%2F86%5C%2Fzz%5C%2FNv87%5C%2F0D" \
                "%5C%2FOv84%5C%2F0v%5C%2FO%5C%2F84%5C%2Fzf%5C%2FMP83%5C%2FzH%5C%2FNv83%5C%2Fzf%5C%2FN%5C%2F84%5C%2Fzf" \
                "%5C%2FOf82%5C%2Fzf%5C%2FOP83%5C%2Fzb%5C%2FMv81%5C%2FzX%5C%2FR%5C%2F9L%5C%2F0v%5C%2FO%5C%2F9I%5C%2F0T" \
                "%5C%2FS%5C%2F9A%5C%2Fzn%5C%2FPf89%5C%2Fzn%5C%2FNf9K%5C%2F07%5C%2FN%5C%2F83%5C%2Fzn%5C%2FNv83%5C%2Fzv" \
                "%5C%2FO%5C%2F9A%5C%2F0H%5C%2FOf8%5C%2F%5C%2Fzj%5C%2FPP83%5C%2Fzj%5C%2FS%5C%2F87%5C%2Fzj%5C%2FNv84%5C" \
                "%2Fzf%5C%2FOf83%5C%2Fzf%5C%2FOf83%5C%2Fzb%5C%2FNv9L%5C%2Fzj%5C%2FNv82%5C%2Fzb%5C%2FN%5C%2F85%5C%2Fzf" \
                "%5C%2FN%5C%2F9J%5C%2Fzf%5C%2FNv83%5C%2Fzj%5C%2FNv84%5C%2F0r%5C%2FSv83%5C%2Fzf%5C%2FMP%5C%2F%5C%2F%5C" \
                "%2Fzb%5C%2FMv82%5C%2Fzb%5C%2FOf85%5C%2Fz7%5C%2FNv8%5C%2F%5C%2F0r%5C%2FS%5C%2F85%5C%2F0H%5C%2FQP9B%5C" \
                "%2F0D%5C%2FNf89%5C%2Fzj%5C%2FOv83%5C%2Fzv%5C%2FNv8%5C%2F%5C%2F0f%5C%2FSv9O%5C%2F0ZeXv%5C%2F%5C%2F%5C" \
                "%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F1X%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C" \
                "%2F%5C%2F%5C%2F%5C%2F9B%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2FTP%5C" \
                "%2F%5C%2F%5C%2F1b%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F0%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C" \
                "%2F%5C%2F%5C%2F%5C%2F%5C%2F9N%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2F%5C%2Fv7%2B%5C%2Fv7%2B" \
                "%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B" \
                "%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B" \
                "%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B" \
                "%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B" \
                "%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B" \
                "%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B" \
                "%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B" \
                "%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B" \
                "%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B" \
                "%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B" \
                "%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B" \
                "%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B" \
                "%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B" \
                "%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B" \
                "%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B" \
                "%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B" \
                "%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B" \
                "%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B" \
                "%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B" \
                "%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B" \
                "%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B" \
                "%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B" \
                "%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B" \
                "%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B" \
                "%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B" \
                "%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B" \
                "%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B" \
                "%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B" \
                "%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%5C%2Fv7%2B%22%2C%22date%22%3A" \
                "%222020-08-14%22%2C%22data%22%3A%5B%7B%22start%22%3A0%2C%22stop%22%3A1439%2C%22value%22%3A" \
                "%22UA8AUBQAUAwAUBoAUAEAYCcAUBkAUB4AUBgAUCAAUAEAUBkAUAwAYAsAYB8AYB0AYBgAYCoAYBgAYB4AUCcAUBsAUB8AUBwA" \
                "UBIAYBkAYB8AUBoAUBMAUCEAUCIAYBYAUBwAUCAAUBgAUCAAUBcAYBsAYCUAATIPYD0KECQAYDMAYB0AYAsAYCAAYDwAYCIAYB0" \
                "AYBcAYCQAYB0AYBAAYCMAYAoAYCIAYCEAYCYAYBsAYBUAYAYAYCIAYCMAUB0AUCAAUBYAUCoAUBEAUC8AUB0AUBYAUDMAUDoAUB" \
                "kAUC0AUBQAUBwAUA0AUBsAUAoAUCEAUBYAUAwAUB4AUAwAUCcAUCYAUCwKYDUAAUUlEC8IYEMAYEgAYDoAYBAAUAMAUBkAWgAAW" \
                "gAAWgAAWgAAWgAAUAgAWgAAUBAAUAQAUA4AUA8AUAkAUAIAUAYAUAcAUAIAWgAAUAQAUAkAUAEAUBkAUCUAWgAAUAYAUBEAWgAA" \
                "UBYAWgAAUAYAWgAAWgAAWgAAWgAAUBcAUAcAWgAAUBUAUAoAUAIAWgAAUAQAUAYAUCgAWgAAUAgAWgAAWgAAUAwAWwAAXCMAUBQ" \
                "AWwAAUAIAWgAAWgAAWgAAWgAAWgAAWgAAWgAAWgAAWREAWQIAUAMAWSEAUDoAUDIAUB8AUCEAUC4AXB4AUA4AWgAAUBIAUA8AUB" \
                "AAUCUAUCIAUAMAUAEAUAsAUAMAUCwAUBYAWgAAWgAAWgAAWgAAWgAAWgAAUAYAWgAAWgAAWgAAUAYAWwAAWgAAUAYAXAQAUAMAU" \
                "BsAUBcAUCAAWwAAWgAAWgAAWgAAWgAAUBgAUB4AWgAAUAcAUAwAWQIAWQkAUAEAUAIAWgAAUAoAWgAAUAYAUB0AWgAAWgAAUAkA" \
                "WgAAWSwAUBIAWgAAUC4AWSYAWgAAUAYAUAoAUAkAUAIAUAcAWgAAUAEAUBEAUBgAUBcAWRYAUA0AWSgAUB4AUDQAUBoAXA4AUA8" \
                "AUBwAUA8AUA4AUA4AWgAAUAIAUCMAWgAAUCwAUBgAUAYAUAAAUAAAUAAAUAAAUAAAUAAAUAAAUAAAUAAAWwAAUAAAcAAAcAAAcA" \
                "AAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAeSEAeQ8Ac" \
                "AAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcBcAcAAAcAAAcCYOcBUAUAAAUAAAUAAAUAAAUAUAUAAAcAAAcAAA" \
                "cAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcCgAeQAAcAAAcAAAcAAAcAAAcAAAcAYAcAAAcBgAeQAAcAA" \
                "AcAAAegAAegAAcAAAcAcAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcCkAeQAAcAcAcAAAcA" \
                "AAcAwAcAAAcAAAcAIAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcCIAeQAAc" \
                "AAAcAAAcAAAcAAAcAAAeRwAeQAAWgAAUAAAUAAAUAAAUAAAUAAAcAAAcAAAcBoAeScAeQAAegAAcBkAeQAAUAAAUAAAUAAAUAAA" \
                "UAAAUAAAcAAAcAAAcAAAcAAAcAAAcAAAegAAegAAcAAAcAAAcBgAeQAAcAAAcAAAcAAAcAAAcAAAcAkAegAAegAAcAcAcAAAcAc" \
                "AcAAAcAAAcAAAcAAAcA8AeQAAcAAAcAAAeRQAcAwAUAAAUAAAUAAAUAAAUAAAUAAAcAAAcBEAcA0AcAAAWQsAUAAAUAAAUAAAUA" \
                "AAUAAAcAAAcAoAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAYAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcBYAegAAcAAAcAAAegAAc" \
                "AcAcAAAcAAAcAAAcAAAcAAAeRkAegAAegAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAEAcAAAcAAAcAAAcAUAcAQAcAAAcBIAeQAA" \
                "cAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcBsAcAAAcAAAcBcAeQAAUAAAUAAAUAAAUAAAUAAAUBQAcBYAUAA" \
                "AUAAAUAoAWRYAWTQAWQAAUAAAUAAAUAAAcAAAcAAAcAAAcAAAcAAAcAMAcAAAcAQAcAAAcAAAcAAAcDMAeSIAcAAAcAAAcAAAcA" \
                "AAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcAAAcBQAeQwAcAAAcAAAcAAAcAMAcAAAeSoAcA8Ac" \
                "DMAcAYAeQoAcAwAcFQAcEMAeVIAaTYAbBcNYAsAYBIAYAIAYAIAYBUAYCwAYBMAYDYAYCkAYDcAUCoAUCcAUAUAUBAAWgAAYBoA" \
                "YBcAYCgAUAMAUAYAUBYAUA4AUBgAUAgAUAgAUAsAUAsAUA4AUAMAUAYAUAQAUBIAASsSUDAAUDAAUBAAYAYAUBAAUAUAUCAAUBo" \
                "AUCAAUBAAUAoAYAIAUAQAUAgAUCcAUAsAUCIAUCUAUAoAUA4AUB8AUBkAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgA" \
                "AfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgA" \
                "AfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgA" \
                "AfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgA" \
                "AfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgA" \
                "AfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgA" \
                "AfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgA" \
                "AfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgA" \
                "AfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgA" \
                "AfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgA" \
                "AfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgA" \
                "AfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgA" \
                "AfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgA" \
                "AfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgA" \
                "AfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgA" \
                "AfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgA" \
                "AfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgA" \
                "AfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgA" \
                "AfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgA" \
                "AfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgA" \
                "AfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgA" \
                "AfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgA" \
                "AfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgA" \
                "AfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgA" \
                "AfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgA" \
                "AfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgA" \
                "AfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgA" \
                "AfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgA" \
                "AfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgA" \
                "AfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgA" \
                "AfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgA" \
                "AfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAAfgAA%22%2C%22tz" \
                "%22%3A32%2C%22did%22%3A%22DA932FFFFE8816E7%22%2C%22src%22%3A24%7D%5D%2C%22summary%22%3A%22%7B%5C%22v" \
                "%5C%22%3A6%2C%5C%22slp%5C%22%3A%7B%5C%22st%5C%22%3A1597349880%2C%5C%22ed%5C%22%3A1597369860%2C%5C" \
                "%22dp%5C%22%3A39%2C%5C%22lt%5C%22%3A294%2C%5C%22wk%5C%22%3A0%2C%5C%22usrSt%5C%22%3A-1440%2C%5C" \
                "%22usrEd%5C%22%3A-1440%2C%5C%22wc%5C%22%3A0%2C%5C%22is%5C%22%3A169%2C%5C%22lb%5C%22%3A10%2C%5C%22to" \
                "%5C%22%3A23%2C%5C%22dt%5C%22%3A0%2C%5C%22rhr%5C%22%3A58%2C%5C%22ss%5C%22%3A69%2C%5C%22stage%5C%22%3A" \
                "%5B%7B%5C%22start%5C%22%3A1698%2C%5C%22stop%5C%22%3A1711%2C%5C%22mode%5C%22%3A4%7D%2C%7B%5C%22start" \
                "%5C%22%3A1712%2C%5C%22stop%5C%22%3A1728%2C%5C%22mode%5C%22%3A5%7D%2C%7B%5C%22start%5C%22%3A1729%2C" \
                "%5C%22stop%5C%22%3A1818%2C%5C%22mode%5C%22%3A4%7D%2C%7B%5C%22start%5C%22%3A1819%2C%5C%22stop%5C%22" \
                "%3A1832%2C%5C%22mode%5C%22%3A5%7D%2C%7B%5C%22start%5C%22%3A1833%2C%5C%22stop%5C%22%3A1920%2C%5C" \
                "%22mode%5C%22%3A4%7D%2C%7B%5C%22start%5C%22%3A1921%2C%5C%22stop%5C%22%3A1928%2C%5C%22mode%5C%22%3A5" \
                "%7D%2C%7B%5C%22start%5C%22%3A1929%2C%5C%22stop%5C%22%3A2030%2C%5C%22mode%5C%22%3A4%7D%5D%7D%2C%5C" \
                "%22stp%5C%22%3A%7B%5C%22ttl%5C%22%3A125%2C%5C%22dis%5C%22%3A82%2C%5C%22cal%5C%22%3A5%2C%5C%22wk%5C" \
                "%22%3A7%2C%5C%22rn%5C%22%3A0%2C%5C%22runDist%5C%22%3A23%2C%5C%22runCal%5C%22%3A3%7D%2C%5C%22goal%5C" \
                "%22%3A8000%2C%5C%22tz%5C%22%3A%5C%2228800%5C%22%2C%5C%22sn%5C%22%3A%5C%22e716882f93da%5C%22%7D%22%2C" \
                "%22source%22%3A24%2C%22type%22%3A0%7D%5D"

    finddate = re.compile(r".*?date%22%3A%22(.*?)%22%2C%22data.*?")
    findstep = re.compile(r".*?ttl%5C%22%3A(.*?)%2C%5C%22dis.*?")
    data_json = re.sub(finddate.findall(data_json)[0], today, str(data_json))
    data_json = re.sub(findstep.findall(data_json)[0], step, str(data_json))

    t = get_time(0)
    s_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(t / 1000)))
    t_1h = int(t / 1000 - 3600)
    url = f"https://api-mifit-cn.huami.com/v1/data/band_data.json?&t={t}"
    head = {
        "apptoken": app_token,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = f"userid={userid}" \
           f"&last_sync_data_time={t_1h}" \
           f"&device_type=0" \
           f"&last_deviceid=default" \
           f"&data_json={data_json}"

    response = requests.post(url, data=data, headers=head).json()
    result = "恭喜! " + response["message"] + f"修改【{name}】的运动步数为: {step}步"
    print(f"[{s_now}][INFO] " + result)
    return result


# 获取时间戳
def get_time(second):
    url = "http://api.m.taobao.com/rest/api3.do?api=mtop.common.getTimestamp"
    response = requests.get(url, headers=headers).json()
    t = int(response["data"]["t"]) - (1000 * second)
    return t


# 获取app_token
def get_app_token(login_token):
    url = f"https://account-cn.huami.com/v1/client/app_tokens" \
          f"?app_name=com.xiaomi.hm.health" \
          f"&dn=api-user.huami.com%2Capi-mifit.huami.com%2Capp-analytics.huami.com" \
          f"&login_token={login_token}"
    response = requests.get(url, headers=headers).json()
    app_token = response["token_info"]["app_token"]
    # print("app_token获取成功!")
    # print(app_token)
    return app_token


# 钉钉机器人推送(实现钉钉机器人推送和艾特关键人)
def push_dd(pkey, pmsg="", mps=[], ids=[], all=False):
    """
    推送消息到钉钉机器人
    """
    if pkey == "":
        print(f"[{now}][WORN]未提供pkey，不进行推送!")
    else:
        server_url = pkey
        param = pmsg

        ding = dd.DingtalkChatbot(server_url)
        json_data = ding.send_text(msg=param, is_at_all=all, at_mobiles=mps, at_dingtalk_ids=ids)

        if json_data["errcode"] == 0:
            print(f"[{now}][SUCCESS]推送成功!")
        else:
            print(f"[{now}][ERROR]推送失败：{json_data['errcode']}({json_data['errmsg']})")


# 推送server酱(将废弃)
def push_wx(pkey, pmsg="", ids=[]):
    """
    推送消息到微信
    """
    if pkey == "":
        print(f"[{now}][WORN]未提供pkey，不进行推送!")
    else:
        server_url = f"https://sc.ftqq.com/{pkey}.send"
        params = {
            "text": "小米运动 步数修改",
            "pmsg": pmsg
        }

        response = requests.get(server_url, params=params)
        json_data = response.json()

        if json_data['errno'] == 0:
            print(f"[{now}][SUCCESS]推送成功!")
        else:
            print(f"[{now}][ERROR]推送失败：{json_data['errno']}({json_data['errmsg']})")


# 推送server酱 新版本
def push_server(pkey, pmsg="", ids=[]):
    """
     推送消息到微信
     """
    if pkey == "":
        print(f"[{now}][WORN]未提供pkey，不进行微信推送!")
    else:
        server_url = f"https://sctapi.ftqq.com/{pkey}.send"
        params = {
            "title": "小米运动 步数修改",
            "pmsg": pmsg
        }

        response = requests.get(server_url, params=params)
        json_data = response.json()
        # print(response)
        # print(json_data)

        if json_data["code"] == 0:
            print(f"[{now}][SUCCESS]推送成功!")
        else:
            print(f"[{now}][ERROR]推送失败：{json_data['code']}({json_data['message']})")


# 推送pushplus
def push_pushplus(token, content=""):
    """
     推送消息到pushplus
     """
    if token == "":
        print(f"[{now}][WORN]未提供token，不进行pushplus推送!")
    else:
        server_url = f"https://www.pushplus.plus/send"
        params = {
            "token": token,
            "title": "小米运动 步数修改",
            "content": content}

        response = requests.get(server_url, params=params)
        json_data = response.json()

        if json_data["code"] == 200:
            print(f"[{now}][SUCCESS]推送成功!")
        else:
            print(f"[{now}] [ERROR]推送失败：{json_data['code']}({json_data['message']})")


# 推送tg
def push_tg(token, chat_id, pmsg=""):
    """
     推送消息到TG
     """
    if token == "":
        print(f"[{now}][WORN]未提供token，不进行tg推送!")
    elif chat_id == "":
        print(f"[{now}][WORN]未提供chat_id，不进行tg推送!")
    else:
        server_url = f"https://api.telegram.org/bot{token}/sendmessage"
        params = {
            "text": "小米运动 步数修改\n\n" + pmsg,
            "chat_id": chat_id
        }

        response = requests.get(server_url, params=params)
        json_data = response.json()

        if json_data["ok"] == True:
            print(f"[{now}][SUCCESS]推送成功!")
        else:
            print(f"[{now}][ERROR]推送失败：{json_data['error_code']}({json_data['description']})")


# 企业微信推送
def push_wxe(msg, usr, corpid, corpsecret, agentid=1000002):
    base_url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?"
    req_url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token="
    corpid = corpid
    corpsecret = corpsecret
    agentid = agentid

    if agentid == 0:
        agentid = 1000002

    # 获取access_token，每次的access_token都不一样，所以需要运行一次请求一次
    def get_access_token(base_url, corpid, corpsecret):
        urls = base_url + "corpid=" + corpid + "&corpsecret=" + corpsecret
        resp = requests.get(urls).json()
        access_token = resp["access_token"]
        return access_token

    def send_message(msg, usr):
        data = get_message(msg, usr)
        req_urls = req_url + get_access_token(base_url, corpid, corpsecret)
        res = requests.post(url=req_urls, data=data)
        ret = res.json()
        if ret["errcode"] == 0:
            print(f"[{now}][SUCCESS]企业微信推送成功!")
        else:
            print(f"[{now}][ERROR]推送失败：{ret['errcode']} 错误信息：{ret['errmsg']}")

    def get_message(msg, usr):
        data = {
            "touser": usr,
            "toparty": "@all",
            "totag": "@all",
            "msgtype": "text",
            "agentid": agentid,
            "text": {"content": msg},
            "safe": 0,
            "enable_id_trans": 0,
            "enable_duplicate_check": 0,
            "duplicate_check_interval": 1800
        }
        data = json.dumps(data)
        return data

    msg = msg
    usr = usr
    if corpid == "":
        print(f"[{now}][WORN]未提供corpid，不进行企业微信推送")
    elif corpsecret == "":
        print(f"[{now}][WORN]未提供corpsecret，不进行企业微信推送")
    else:
        send_message(msg, usr)


class Push:
    def __init__(self, pmode, pmsg, ids, token):
        # Push Key 推送开关: 钉钉、微信、企业微信等
        # pkey = "https://oapi.dingtalk.com/robot/send?access_token" \
        #        "=c68c392bd46d79145ffb52ef2e589f75120d42a41260de354a540080eeb8fcbe"  # 钉钉机器人推送
        # pkey = "SCT4767TsSiDGVriYP8CCD2zbUBbvRVo"  # 微信/server酱
        if pmode == "钉钉":
            timestamp = str(round(time.time() * 1000))
            secret = "SEC317f5041deddcc34b8890b0383aec4cafe231907723489feb0b91b8bd4a3307f"
            secret_enc = secret.encode("utf-8")
            string_to_sign = "{}\n{}".format(timestamp, secret)
            string_to_sign_enc = string_to_sign.encode("utf-8")
            hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
            sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
            token = "c68c392bd46d79145ffb52ef2e589f75120d42a41260de354a540080eeb8fcbe"
            pkey = "https://oapi.dingtalk.com/robot/send" \
                   f"?access_token={token}" \
                   f"&timestamp={timestamp}" \
                   f"&sign={sign}"
            if pkey.find("https://oapi.dingtalk.com/robot") == -1 or pkey.find("access_token") == -1:
                print("钉钉机器人Webhook有误, 请检查!")
            else:
                push_dd(pkey, pmsg, ids)
        elif pmode == "微信":
            pkey = "SCT4767TsSiDGVriYP8CCD2zbUBbvRVo"
            if pkey.find("SCT") == -1:
                print("微信SCKEY有误, 请检查!")
            push_wx(pkey, pmsg)
        elif pmode == "Server酱":
            # ServerChan
            pkey = "SCT4767TsSiDGVriYP8CCD2zbUBbvRVo"
            if pkey.find("SCT") == -1:
                print("微信SCKEY有误, 请检查!")
            else:
                push_server(pkey, pmsg)
        elif pmode == "电报":
            tokens = token.split("@")
            if len(tokens) == 3:
                push_tg(tokens[0], tokens[1], pmsg)
            else:
                print(f"[{now}][ERROR]Token按[@]拆分后参数数量不正确!")
        elif pmode == "企业微信":
            tokens = token.split("-")
            if len(tokens) == 3:
                push_wxe(pmsg, tokens[0], tokens[1], tokens[2])
            elif len(tokens) == 4:
                push_wxe(pmsg, tokens[0], tokens[1], tokens[2], int(tokens[3]))
            else:
                print(f"[{now}][ERROR]Token按[-]拆分后参数数量不正确!")
        elif pmode == "接口":
            if token == "":
                print("PushPlus Token为空, 请补充!")
            elif token == "":
                print("PushPlus Token为空, 请补充!")
            else:
                push_pushplus(token, pmsg)
        elif pmode == "关闭":
            print("不推送")
        else:
            print(f"[{now}][ERROR]推送选项有误! 默认选择不推送")
            exit(0)


if __name__ == "__main__":
    print(f"[{now}][INFO]: Motion 已经启动、加载并运行!"
          f"他将持续几秒钟, 请耐心稍候!")
    print(f"[{now}][INFO]: Motion Has Started And Load And Been Running"
          f"It Will Take A Little Seconds, Please Keep Patient!")

    # 用户名: 电话号码
    users = []
    # 用户姓名
    names = []
    # 用户密码
    pwds = []
    # 用户步数范围: 要修改的步数，直接输入想要修改的步数值，留空为随机步数
    # steps = [80980, 89980]
    steps = [40980, 48980]

    # 推送选项 Push Mode
    pmode = "钉钉"
    #
    pmsg = "Hello! 今天的步数更新啦![摸摸]"
    # 通知人钉钉
    ids = []
    # 通知token
    token = ""

    # Motion 正式运行
    if len(users) == len(pwds):
        for line in range(0, len(users)):
            if len(steps) == 2:
                step = random.randint(steps[0], steps[1])
            elif len(steps) == 1:
                step = steps[0]
            else:
                step = random.randint(80980, 89980)  # 自己使用的默认步数
            step = str(int((int(now[11:13]) - random.random()) / 20 * step))  # 按照[时间：时]和[随机数]计算步数
            # step = str(int((int(now[11:13]) + int(now[14:16])/60 + int(now[17:19])/3600)/20 * step)) # 按照[时间：时分秒]计算步数
            response = main(users[line], pwds[line], names[line], step)
            pmsg += "\n" + response.replace("success", "成功")
        Push(pmode, pmsg, ids, token)
    else:
        print(f"[{now}][ERROR]用户名数和密码数不相等")
