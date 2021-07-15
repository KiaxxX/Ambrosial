# code=utf-8


# 不换行print
def print_line(p):
    print(p, end="")
    return


def while_func(p):
    i = p
    while i > 0:
        print_line(i), print_line(":"), print(i % 2)
        i -= 1


def for_func(p):
    for f in p:
        print_line("当前字母:"), print(f)


# 素数(质数)判断
def cicle_func(p):
    print("我们来求: " + p + "是su shu")
    while p > 1:
        flag = 1
        if p == 25:
            print("25:是非素数,这是我事先知道的,跳过")
        else:
            pass
        for i in range(2, p - 1):
            if p % i == 0:
                flag = 0
                break
            else:
                pass
        if flag == 1:
            print_line(p), print(":是素数")
        else:
            print_line(p), print(":是非素数")
        p -= 1
    print("1:既不是素数，也不是非素数")


# 字符串尝试
def str_func():
    print_line("输出字符串: "), print("你是一个小可爱\t你是一个大聪明")
    print_line("原始字符串: "), print(R"你是一个小可爱\t你是一个大聪明")


# 字符串格式化尝试
def strFormat_func(p, y):
    print("%s要喜欢陈新平%d年！" % (p, y))


# 三引号使用尝试
def strThreeQuote_func():
    str = '''你好 -- 
你好  你好
    你好  你好\n'''
    strR = R'''你好 -- \
你好  你好
    你好  %s\n''' % "你好"
    print(str)
    print("==========")
    print(strR)


# 标题化使用尝试
def strTitle_func(p):
    print(p)
    print(p.istitle())
    print(p.title())
    print(p.title().istitle())


# List结构尝试
def list_func(p):
    for i in p:
        print_line(i)
    print("试一试: 分开输出")  # 末尾换行


# 字典结构尝试(未完成)
def dict_func(p):
    print(len(p))
    print(p["name"])
    print("dict is:" + str(p))


if __name__ == '__main__':
    # while_func(100)
    # for_func("myName")
    # cicle_func(50)
    # strrR_func()
    # strFormat_func("李凯华", 1000)
    # strThreeQuote_func()
    # strTitle_func("my Name Is Karsa")
    # list_func(["Likaihua ", "is ", "a ", "boy ", "!"])
    dict_func({"name" : "Likaihua ","action" : "is ","quantifier" : "a ","noun" : "boy ","punctuation" : "!"})
    print_line("===Func Is Over, Bay-bay===")
