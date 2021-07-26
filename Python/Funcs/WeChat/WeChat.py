# -*- coding: utf8 -*-
# python >=3.8
import itchat
from itchat.content import *

if __name__ == "__main__":
    print("开始!")
    itchat.auto_login(hotReload=False)
    friends_list = itchat.get_friends(update=True)
    print(friends_list)
    name = itchat.search_friends(name=u"果")
    print(name)