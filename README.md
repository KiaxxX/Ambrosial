# 一、Python项目
## 初识python
> 主要功能: 小米运动自动刷步数、淘宝天猫抢购

### Python学习项目
0. 仅供学习
1. 共同学习欢迎, 抄袭商用可耻

### 小米运动自动刷步数(Python/Funcs/Motion)
0. 代码由方块君发布, 本处只做对自己有用之改良, 请自行到方块君处 Fork：https://github.com/577fkj/mimotion
1. 用于学(zhuang)习(B) 系统化的Python项目

### 邮件(Python/Funcs/SendMails)
1. 邮件的基础形式
2. 可以自行设置邮件内容(需要有一定的编码基础)

### 表白HTML(Confession/)
1. 除供学习外, 逗小可爱开心
2. 使用时: a,更改好文本

# 二、java项目
## ja-netfilter项目配置
> 用于学习、熟悉、使用某些商用开发软件, 以进一步购买!!!

### 项目地址
```CONF
    # 主项目 ja-netfilter
URL = https://github.com/ja-netfilter/ja-netfilter

    # 插件项目 plugins: dns, url, hideme, power, mymap
URL = https://github.com/ja-netfilter/plugin-dns
URL = https://github.com/ja-netfilter/plugin-url
URL = https://github.com/ja-netfilter/plugin-hideme
URL = https://github.com/ja-netfilter/plugin-power
URL = https://github.com/zfkun/ja-netfilter-mymap-plugin
```

###janf_config.txt 配置内容
```CONF
[DNS]
EQUAL,jetbrains.com

[URL]
    # JetBrain
PREFIX,https://account.jetbrains.com/lservice/rpc/validateKey.action
    # DBEaver
PREFIX,https://dbeaver.com/lmp/checkLicense
    # SmartGit
PREFIX,https://store.smartgit.com/check

[MyMap]
EQUAL,licenseeName->李凯华
EQUAL,gracePeriodDays->30
EQUAL,paidUpTo->2025-12-31
```

###使用细则
1. 创建文件夹: [ja-netfilter]
2. 在文件夹: [ja-netfilter] 下创建文件夹: [plugins]
3. 在文件夹: [ja-netfilter] 下创建文件: janf_config.txt
4. 将主项目 ja-netfilter.jar 放置文件夹: [ja-netfilter]
5. 将插件项目 plugins 的所有jar包 放置文件夹: [plugins]
6. 填写 <janf_config.txt 配置内容> 到 janf_config.txt
7. 将文件夹: [ja-netfilter] 移动到目录: [{目录}/ja-netfilter]
8. 在 JetBrain 项目的 xxx.vmoptions 文件追加: -javaagent:{目录}/ja-netfilter/ja-netfilter.jar