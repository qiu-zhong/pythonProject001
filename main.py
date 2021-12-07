# 这是一个发送邮件的简单实例 。
# !/usr/bin/python310
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'from@JJ.com'
receiver = ['zq.2021@qq.com']

# 三个参数：第一个是文本内容，第二个plain设置文本格式，第三个设置编码
message = MIMEText('Python 邮件发送测试。。。', 'plain', 'utf-8')
message['From'] = Header("JJ", 'utf-8')  # 发送者
message['TO'] = Header("测试", 'utf-8')  # 接收者

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receiver, message.as_string())
    print("邮件发送成功")
except smtplib.SMTPException:
    print("Error：无法发送邮件")
