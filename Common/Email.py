# -*- coding: utf-8 -*-
# @Time   :2019/08/30
# @Author    : chenyue
"""
封装发送邮件方法
"""
import smtplib
import time
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Common import Consts,Log
from Config import Config
import os


class SendMail:
    def __init__(self):
        self.config = Config.Config()
        self.log = Log.MyLog()

    @staticmethod
    def latest_report(report_dir):
        # os.listdir()方法用于返回指定文件夹包含文件或文件夹的名字列表
        lists=os.listdir(report_dir)
        # 按照时间顺序对该目录文件夹下面的文件进行排序
        lists.sort(key=lambda fn:os.path.getatime(report_dir+'\\'+fn))
        # 输出最新的报告路径
        file = os.path.join(report_dir,lists[0])
        return file

    def send_mail(self):
        report = SendMail.latest_report('..\Reports')
        with open(report, 'rb') as e:
            body = e.read()
        e.close()
        msg = MIMEMultipart()
        # stress_body = Consts.STRESS_LIST
        # result_body = Consts.RESULT_LIST
        # body = 'Hi,all\n本次接口自动化测试报告如下:\n  接口响应集:%s\n  接口运行结果集:%s' % (stress_body, result_body)
        mail_body2 = MIMEText(body, 'html', 'utf-8')
        tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        msg['Subject'] = Header("接口自动化测试报告" + "_" + tm, 'utf-8')
        msg['From'] = self.config.sender
        receivers = self.config.receiver
        toclause = receivers.split(',')
        msg['To'] = ",".join(toclause)
        msg.attach(mail_body2)
        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.config.smtpserver)
            smtp.login(self.config.username, self.config.password)
            smtp.sendmail(self.config.sender, toclause, msg.as_string())
            smtp.quit()
        except smtplib.SMTPException as e:
            print(e)
            print("发送失败")
            self.log.error("邮件发送失败，请检查邮件配置")
        else:
            print("发送成功")
            self.log.info("邮件发送成功")


if __name__ == "__main__":
    last = SendMail()
    last.send_mail()
    # last = SendMail()
    # print(last.config.smtpserver,last.config.username,last.config.password,last.config.sender,last.config.receiver)
