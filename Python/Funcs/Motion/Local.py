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
    # pmsg = "发布新版, 软件信息:"
    # pmsg += "\n版本: 0.2.21  版权所有: 李凯华" \
    #         "\n更新内容:" \
    #         "\n\t1,更新钉钉推送逻辑, 信息安全保证" \
    #         "\n\t2,提高代码健壮性, 更加稳定产出" \
    #         "\n\t3,修复无法钉钉通知问题【反馈：20210805201044】" \
    #         "\n\t\t-将在今日20:30发起补充脚本(完成)" \
    #         "\n\t4,增加一个新表情, 摸头杀[摸摸], 放弃[烟花], 后续可以更新其他表情" \
    #         "\n更多新特性体验, 欢迎尝试和建议..."
    # pmsg = f"动态发布[{time.time()}]:"
    # pmsg += "\n\t因任务步数增多, 支付宝渠道不接受频繁的步数变更, 任务将在3日内作出合理化调整!" \
    #         "\n\t任务临时暂停, 初步订7日后开放" \
    #         "\n\t具体调整完成时间将在此群同步, 敬请关注......"
    pmsg = "Something ERROR! Please chack in!"
    while(True):
        # time.sleep(3600)
        # push_dd(pkey, pmsg, all=True)
        push_dd(pkey, "测试!", mps=[17864307818])
        time.sleep(7)