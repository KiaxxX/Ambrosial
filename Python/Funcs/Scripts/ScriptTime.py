# code=utf-8
import datetime


# 倒序输出时间(用以打印连续日期的脚本)
def scriptTimeReverse(the_day, key_day):
    if the_day < key_day:
        the_day, key_day = key_day, the_day
    the_date = datetime.datetime.strptime(the_day, "%Y-%m-%d")
    key_date = datetime.datetime.strptime(key_day, "%Y-%m-%d")
    while key_date <= the_date <= datetime.datetime.now():  # 日期小于现在时间(否则将无限输出)
        the_year = the_date.strftime("%Y")
        the_mon = the_date.strftime("%Y-%m")
        the_day = the_date.strftime("%Y-%m-%d")
        printScriptTime(the_year, the_mon, the_day)
        the_date = the_date - datetime.timedelta(days=1)  # 按照时间逆序输出


# 这里填写打印脚本
def printScriptTime(the_year, the_mon, the_day):
    # print(
    #     "nohup bash ${tools_dir}/beeline_exec_hql.sh -f ${root_dir}/dw_etl/dm/chat/dm.dm_chatsess_retain_sd.hql -t "
    #     + the_day
    #     + " &"
    # ) # 填充Script
    # print(
    #     "nohup bash ${tools_dir}/beeline_exec_hql.sh -f ${root_dir}/dw_etl/dm/chat/dm.dm_chatsess_source_sd.hql -t "
    #     + the_day
    #     + " &"
    # ) # 填充Script
    # print(
    #     "nohup bash ${tools_dir}/beeline_exec_hql.sh -f ${root_dir}/dw_etl/dm/chat/dm.dm_chatuser_complainted_sd.hql -t "
    #     + the_day
    #     + " &"
    # )  # 填充Script
    # print(
    #     "nohup bash ${tools_dir}/beeline_exec_hql.sh -f ${root_dir}/dw_etl/dw/chat/dw.dw_chatuser_sess_cnt_sd.hql -t "
    #     + the_day
    #     + " &"
    # )  # 填充Script
    print(
        "nohup bash ${tools_dir}/beeline_exec_hql.sh -f ${root_dir}/dw_etl/dm/chat/dm.dm_chat_match_summary_sd.hql -t "
        + the_day
        + " &"
    )  # 填充Script


if __name__ == '__main__':
    scriptTimeReverse("2021-06-02", "2021-07-08")
