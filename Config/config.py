# -*- coding: utf-8 -*-
# @Time   :2019/08/12
# @Author    : chenyue

from configparser import ConfigParser
from CaibeikeAPItest.Common import Log
import os


class Config:
    # titles:
    TITLE_DEBUG = "PRE_DEBUG"
    TITLE_RELEASE = "MAPI_DEBUG"
    TITLE_MAIL = "mail"

    # values:
    # [PRE\MAPI]
    VALUE_TESTER = 'tester'
    VALUE_ENVIRONMENT = 'environment'
    VALUE_VERSION_CODE = 'versionCode'
    VALUE_HOST = 'host'
    VALUE_LOGIN_HOST = 'loginHost'
    VALUE_LOGIN_INFO = 'loginInfo'

    # [MAIL]
    VALUE_SMTP_SERVER = 'smtpserver'
    VALUE_SENDER = 'sender'
    VALUE_RECEIVER = 'receiver'
    VALUE_USERNAME = 'username'
    VALUE_PASSWORD = 'password'

    # path
    path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

    def __init__(self):
        """
        初始化
        """
        self.config = ConfigParser()
        self.log = Log.MyLog()
        self.conf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.ini')
        self.xml_report_path = Config.path_dir + '/Report/xml'
        self.html_report_path = Config.path_dir + '/Report/html'

        if not os.path.exists(self.conf_path):
            raise FileNotFoundError("请确保配置文件存在！！！")
        self.config.read(self.conf_path, encoding='utf-8')

        self.tester_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_TESTER)
        self.environment_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_ENVIRONMENT)
        self.versionCode_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_VERSION_CODE)
        self.host_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_HOST)
        self.loginHost_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_LOGIN_HOST)
        self.loginInfo_debug = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_LOGIN_INFO)

        self.tester_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_TESTER)
        self.environment_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_ENVIRONMENT)
        self.versionCode_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_VERSION_CODE)
        self.host_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_HOST)
        self.loginHost_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_LOGIN_HOST)
        self.loginInfo_release = self.get_conf(Config.TITLE_RELEASE, Config.VALUE_LOGIN_INFO)

        self.smtpserver = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_TESTER)
        self.sender = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_TESTER)
        self.receiver = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_TESTER)
        self.username = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_TESTER)
        self.password = self.get_conf(Config.TITLE_DEBUG, Config.VALUE_TESTER)

    def get_conf(self, title, value):
        """
        读取配置文件
        :param title:
        :param value:
        :return:
        """
        return self.config.get(title, value)

    def set_conf(self, title, value, text):
        """
        修改配置文件
        :param title:
        :param value:
        :param text:
        :return:
        """
        self.config.set(title, value, text)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)

    def add_conf(self, title):
        """
        添加配置文件
        :param title:
        :return:
        """
        self.config.add_section(title)
        with open(self.conf_path, "w+") as f:
            return self.config.write(f)
