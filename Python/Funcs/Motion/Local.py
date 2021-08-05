# -*- coding: utf8 -*-
# python >=3.8
import urllib.parse
from Python.Funcs.Motion.Motion import *

if __name__ == "__main__":
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
    pmsg = "软件信息:"
    pmsg += "\n版本: 0.2.16  版权所有: 李凯华" \
            "\n更新内容:" \
            "\n\t1,更新钉钉推送逻辑，提高信息的安全性" \
            "\n\t2,提高代码健壮性" \
            "\n\t3,修复无法钉钉通知问题" \
            "\n\t\t将在今日20:30发起补充脚本" \
            "\n\t更多新特性体验, 欢迎尝试和建议..."
    # pmsg += "\n 因版本更新, 最新的消息已被屏蔽! 预计明天修复..."
    push_dd(pkey, pmsg)
