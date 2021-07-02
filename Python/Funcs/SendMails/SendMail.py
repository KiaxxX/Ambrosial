# coding=utf-8
import sys
import logging
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os

from importlib import reload

reload(sys)


def usage():
    print("Usage: %s -t <TEXT|PLAIN|TABLE> -s subject -c content -i fileheader -f file -r receivers -a attachment -x "
          "ccreceivers" %
          sys.argv[0])


def sendmail(receivers, subject, content):
    logging.info("send mail:%s" % locals())
    sendmail_imp('smtp.qq.com', '1366271024@qq.com', 'xccbupkuuybybafh', receivers, None, subject, content, [])   # QQ邮箱


def sendmail_imp(host, sender, pwd, receivers, receivers_cc, subject, content, files):
    print('INFO: Sending mail ...')

    mail = MIMEMultipart()
    mail_host = host  # 服务器
    mail_user = sender  # 发件人
    mail_pass = pwd  # 发件人口令
    mail_receivers = receivers  # 收件人 - 数组
    mail_receivers = receivers_cc  # 抄送人 - 数组
    mail_subject = subject  # 主题
    mail_content = content  # 内容
    mail_files = files  # 附件 - 数组

    # 添加内容
    message = MIMEText(content, 'html', 'utf-8')
    mail.attach(message)

    # 添加附件
    for filex in files:
        if filex is not None:
            attachment = MIMEApplication(open(filex, 'rb').read())
            attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(filex))
            mail.attach(attachment)
    mail['From'] = Header("Assistant", 'utf-8')
    mail['To'] = ';'.join(receivers)
    if receivers_cc is not None:
        mail['Cc'] = Header(';'.join(receivers_cc), 'utf-8')
    mail['Subject'] = Header(subject, 'utf-8')

    try:
        smtp_obj = smtplib.SMTP_SSL(host, 465)
        smtp_obj.ehlo()
        # smtp_obj.esmtp_features["auth"] = "LOGIN PLAIN"
        # smtp_obj.connect(host, 25)  # 25 为 SMTP 端口号
        smtp_obj.login(sender, pwd)  # "xccbupkuuybybafh"
        smtp_obj.sendmail(sender, receivers, mail.as_string())
        print('''INFO: Mail has been sent, Congratulations!''')
    except Exception as e:
        print('''ERROR: Can`t send the mail, becouse some unknow problems! You can read the tips following.''')
        print(e)


# 判断形式(暂不使用)
def construct_body(typ, file_header, filex):
    if typ == 'TABLE':
        return construct_table(file_header, filex)
    elif typ == 'PLAIN':
        return construct_plain(file_header, filex)
    else:
        print('''Error: Unknown delivery type! Please confirm the type is in "TABLE" or "PLAIN"!''')


# 表格(暂不使用)
def construct_table(file_header, filex):
    table = '<table border="1">'

    table += '  <tr>'
    for h in file_header.split(','):
        table += '<th>%s</th>' % h
    table += '  </tr>'

    with open(filex, 'r') as f:
        for line in f:
            table += '  <tr>'
            for c in line.split('\t'):
                table += '<td>%s</td>' % c
            table += '  </tr>'

    table += '</table>'

    return table


# 段落(白话)
def construct_plain(file_header, filex):
    with open(filex, 'r') as f:
        lines = [file_header] + f.readlines()
        return '<br />'.join(lines)
