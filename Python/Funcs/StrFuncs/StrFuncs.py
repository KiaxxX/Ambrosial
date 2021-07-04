# code=utf-8


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


if __name__ == '__main__':
    # capitalizeFunc("likaihua") # Likaihua
    # print(returnFunc("likai"))
    # centerFunc("likaihua")
    # countFunc("likaihua17864307818", 8)
    # endwithFunc("likaihua", "hua")
    printLine("===Func Is Over, Bay-bay===")
