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
from CaibeikeAPItest.Common import Consts,Log
from CaibeikeAPItest.Config import Config


class SendMail:
    def __init__(self):
        self.config = Config()
        self.log = Log.MyLog()

    def sendMail(self):
        msg = MIMEMultipart()

        stress_body = Consts.STRESS_LIST
        result_body = Consts.RESULT_LIST
        body2 = 'Hi,all\n本次接口自动化测试报告如下:\n  接口响应集:%s\n  接口运行结果集:%s' % (stress_body, result_body)
        mail_body2 = MIMEText(body2, _subtype='plain', _charset='utf-8')
        tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        msg['Subject'] = Header("接口自动化测试报告" + "_" + tm, 'utf-8')
        msg['From']  = self.config.sender
        receivers = self.config.receiver
        toclause = receivers.split(',')
        msg['To'] = ",".join(toclause)

        msg.attach(mail_body2)
        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.config.smtpserver)
            smtp.login(self.config.username, self.config.password)
            smtp.sendmail(self.config.sender, toclause, msg.as_string())
        except Exception as e:
            print(e)
            print("发送失败")
            self.log.error("邮件发送失败，请检查邮件配置")
        else:
            print("发送成功")
            self.log.info("邮件发送成功")
        finally:
            smtp.quit()
