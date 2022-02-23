# code=udf-8
import datetime
from Python.Funcs.SendMails import SendMail1 as sendMail


def is_number(s):
    try:
        num = float(s)
        if num > 1:
            return False
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False


# 邮件内容编编辑
def send(now_time):
    """
        邮件内容的编辑!
    """
    rows = '''2021-05-01 04:12:30 坐公交车到家 济南 李凯华 100 0.9612087818 必须 
2021-05-01 04:12:30  济南 李凯华 100 0.0612087818 必须 
2021-05-01 04:12:30 坐公交车到家 济南 李凯华 100  必须 '''
    html_str = ""
    html_str += """
<h3> 我的日历 %s</h3><table border=1>
    <tr>
        <td>日期</td>
        <td>时间</td>
        <td>事件</td>
        <td>地点</td>
        <td>人物</td>
        <td>消费</td>
        <td>进度</td>
        <td>标注</td>
        <td>备注</td>
    </tr>""" % now_time
    rows = rows.split("\n")
    print(rows)
    for rowKeys in rows:
        row = rowKeys.split(" ")
        html_str += "<tr>"
        for i in range(0, 9):
            html_str += "\n\t\t"
            if i in [0, 1, 2, 3, 4, 5, 7, 8]:  # 不转化为百分比
                if row[i] is None or row[i] == "":
                    html_str += "<td>无</td>"
                else:
                    html_str += "<td>%s</td>" % row[i]
            else:   # 哪些行转为百分比
                if row[i] is None or row[i] == "":
                    html_str += "<td>00.00%</td>"
                else:
                    html_str += "<td>%.2f%%</td>" % (float(row[i]) * 100)
    html_str += "\n\t</tr>\n</h3>"

    print(html_str)
    sendMail.sendmail(["name@soulapp.cn"], "测试邮件[%s]" % datetime.datetime.now().strftime("%Y-%m-%d"), html_str)


if __name__ == '__main__':
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    send(now)
