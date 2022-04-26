# code=utf-8
import datetime
import time


# 倒序输出时间(用以打印连续日期的脚本)
def scriptTimeReverse(the_day, key_day=time.strftime("%Y-%m-%d", time.localtime())):
    if the_day > key_day: # 按照时间顺序输出
        # if the_day < key_day: # 按照时间逆序输出
        the_day, key_day = key_day, the_day
    the_date = datetime.datetime.strptime(the_day, "%Y-%m-%d")
    key_date = datetime.datetime.strptime(key_day, "%Y-%m-%d")
    while datetime.datetime.now() >= key_date >= the_date: # 按照时间顺序输出
        # while key_date <= the_date <= datetime.datetime.now():  # 按照时间逆序输出
        the_year = the_date.strftime("%Y")
        the_mon = the_date.strftime("%Y-%m")
        the_day = the_date.strftime("%Y-%m-%d")
        printScriptTime(the_year, the_mon, the_day)
        the_date = the_date + datetime.timedelta(days=1)    # 按照时间顺序输出
        # the_date = the_date - datetime.timedelta(days=1)  # 按照时间逆序输出


# 这里填写打印脚本
def printScriptTime(the_year, the_mon, the_day):
    print(
        "nohup" + " "
        + ""  # 填充Script
        + " " + the_day + " " + "&"
    )


if __name__ == '__main__':
    scriptTimeReverse("2021-12-31", "2021-08-01")
