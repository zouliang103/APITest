# -*- coding: utf-8 -*-
# @Time   :2019/08/30
# @Author    : chenyue

""""

"""
import sys
import os
import pytest
from Common import Log, shell, Email
from Config import Config
from Params import params
if __name__ == '__main__':
    # a = os.getcwd()
    now_file_name = os.path.abspath(os.path.dirname(__file__))
    testcase_file_name = now_file_name + '\TestCase'
    os.chdir(testcase_file_name)
    conf = Config.Config()
    log = Log.MyLog()
    log.info('初始化配置文件,path=' + conf.conf_path)
    shell = shell.Shell()
    report_name = params.GetParam.new_report_name()
    # 定义测试集
    cmd = 'pytest --html=../Reports/%s.html --self-contained-html' % report_name
    try:
        shell.invoke("cd TestCase")
        shell.invoke(cmd)
    except Exception as e:
        log.error('执行用例失败，请检查环境配置')
        raise

    try:
        mail = Email.SendMail()
        mail.send_mail()
    except Exception as e:
        log.error('发送邮件失败，请检查邮件配置')
        raise
