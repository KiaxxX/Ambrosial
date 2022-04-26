# code=utf-8
import re


# 不换行print(实用)
def printLine(p):
    print(p, end="")


def returnFunc(p) -> str:  # 判断一个人长得抽还是帅
    if p == "likaihua" or p == "李凯华":
        return p + "真帅!"
    else:
        return p + "还行!"


def capitalizeFunc(p: str):
    print(p.capitalize())


def centerFunc(p: str):
    print(p.center(20, "="))


def countFunc(p: str, ch):
    ch = str(ch)
    c: int = p.count(ch, 0, len(p))
    print(c)


def endwithFunc(p:str, ch):
    if p.endswith(ch, 0, len(p)):
        print("[" + ch + "]是[" + p + "]的结尾!")
    else:
        print("[" + ch + "]不是[" + p + "]的结尾!")

def getFeilds(sql):
    str = sql.replace("\n", "")
    while str.find("  ") != -1:
        str = str.replace("  ", " ");
    res = re.match(r'select (.*) from', str.lower().strip()).group(1).split(",")
    files = []
    for r in res:
        if r.find(" as ") != -1:
            files.append(r.split(" as ")[1].strip())
        else:
            files.append(r.strip())
    return files


if __name__ == '__main__':
    # capitalizeFunc("likaihua") # Likaihua
    # print(returnFunc("likai"))
    # centerFunc("likaihua")
    # countFunc("likaihua17864307818", 8)
    # endwithFunc("likaihua", "hua")

    sql = """
        select 
            song_id, song_name, sum(hot_score) as socre
        from rpt.rpt_soc_voiceroom_ktv_song_sd 
        where day>= '{day}'
        group by song_id, song_name
        limit 1
    """
    bootstrap_servers='realtime-kafka01.soulapp.cn:9092,' \
                      'realtime-kafka02.soulapp.cn:9092,' \
                      'realtime-kafka03.soulapp.cn:9092,' \
                      'realtime-kafka04.soulapp.cn:9092,' \
                      'realtime-kafka05.soulapp.cn:9092,' \
                      'realtime-kafka06.soulapp.cn:9092,' \
                      'realtime-kafka07.soulapp.cn:9092,' \
                      'realtime-kafka08.soulapp.cn:9092,' \
                      'realtime-kafka09.soulapp.cn:9092,' \
                      'realtime-kafka10.soulapp.cn:9092'


    printLine("===Func Is Over, Bay-bay===")
