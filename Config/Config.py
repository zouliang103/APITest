# -*- coding: utf-8 -*-
# @Time   :2019/08/12
# @Author    : chenyue

from configparser import ConfigParser
from Common import Log
import os


class Config:
    # titles:
    TITLE_DEBUG = "PRE_DEBUG"
    TITLE_RELEASE = "MAPI_DEBUG"
    TITLE_MAIL = "mail"
    TITLE_Mongodb = "Mongodb"
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
    # MongoDb config
    VALUE_MD_HOST = "host"
    VALUE_MD_PORT = "port"
    VALUE_MD_USERNAME = "username"
    VALUE_MD_PASSWORD = "password"
    VALUE_MD_DATABASE = "database"
    VALUE_MD_SSHADD = "sshAddress"
    VALUE_MD_SSHUSERNAME = "sshUserName"
    VALUE_MD_SSHPWD = "sshUserPwd"

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

        self.smtpserver = self.get_conf(Config.TITLE_MAIL, Config.VALUE_SMTP_SERVER)
        self.sender = self.get_conf(Config.TITLE_MAIL, Config.VALUE_SENDER)
        self.receiver = self.get_conf(Config.TITLE_MAIL, Config.VALUE_RECEIVER)
        self.username = self.get_conf(Config.TITLE_MAIL, Config.VALUE_USERNAME)
        self.password = self.get_conf(Config.TITLE_MAIL, Config.VALUE_PASSWORD)

        self.md_host = self.get_conf(Config.TITLE_Mongodb ,Config.VALUE_MD_HOST)
        self.md_port = self.get_conf(Config.TITLE_Mongodb, Config.VALUE_MD_PORT)
        self.md_username = self.get_conf(Config.TITLE_Mongodb, Config.VALUE_MD_USERNAME)
        self.md_password = self.get_conf(Config.TITLE_Mongodb, Config.VALUE_MD_PASSWORD)
        self.md_database = self.get_conf(Config.TITLE_Mongodb, Config.VALUE_MD_DATABASE)
        self.md_ssh_add = self.get_conf(Config.TITLE_Mongodb,Config.VALUE_MD_SSHADD)
        self.md_ssh_username = self.get_conf(Config.TITLE_Mongodb,Config.VALUE_MD_SSHUSERNAME)
        self.md_ssh_pwd = self.get_conf(Config.TITLE_Mongodb,Config.VALUE_MD_SSHPWD)

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


if __name__ == "__main__":
    cg = Config()
    print(cg.md_host,cg.md_port,cg.md_username,cg.md_password,cg.md_database,
          cg.md_ssh_add,cg.md_ssh_username,cg.md_ssh_pwd)
