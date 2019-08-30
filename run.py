# -*- coding: utf-8 -*-
# @Time   :2019/08/30
# @Author    : chenyue

""""
运行测试集
# '--allure_severities=critical, blocker'
# '--allure_stories=测试模块_demo1, 测试模块_demo2'
# '--allure_features=测试features'
"""
import sys
import pytest
from CaibeikeAPItest.Common import Log,shell,Email
from CaibeikeAPItest.Config import Config

if __name__ == '__main__':
    conf = Config.Config()
    log = Log.MyLog()
    log.info('初始化配置文件,path=' + conf.conf_path)

    shell = shell.Shell()
    xml_report_path = conf.xml_report_path
    html_report_path = conf.html_report_path

    # 定义测试集
    args = ['-s', '-q', '--allure', xml_report_path]
    pytest.main(args)
    cmd = 'allure generate %s -o %s' % (xml_report_path, html_report_path)

    try:
        shell.invoke(cmd)
    except Exception as e:
        log.error('执行用例失败，请检查环境配置')
        raise

    try:
        mail = Email.SendMail()
        mail.sendMail()
    except Exception as e:
        log.error('发送邮件失败，请检查邮件配置')
        raise
