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
    # print(
    #     "nohup" + " "
    #     + "bash ${tools_dir}/exec_hql.sh -f  ${root_dir}/dw_etl/dm/soc/dm.dm_soc_voiceroom_user_sd.hql -t"  # 填充Script
    #     + " " + the_day + " " + "&"
    # )
    print(
        "alter table mbadp.t_dw_news_industry_car_user_behavior add if not exists partition(dt='" + the_day.replace('-','') + "', source='app') "
        + "location 'hdfs://router/user/mbadp/hive/warehouse/t_dw_news_industry_car_user_behavior/history/dt=" + the_day.replace('-','') + "/source=app';"
    )
    # print(
    #     "/user/mbadp/hive/warehouse/t_dwd_adp_profile_app_list_d/dt=" + the_day.replace('-','') + ""
    # )


if __name__ == '__main__':
    scriptTimeReverse("2024-10-01")
    # times = '2022-10-10 01:12:12'
    # time  = datetime.datetime.strptime(times, '%Y-%m-%d %H:%M:%S')
    # cday = time.strftime('%Y-%m-%d')
    # print(cday)
    # ctime = time.strftime('%H')
    # print(ctime)


