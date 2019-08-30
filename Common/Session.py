# -*- coding: utf-8 -*-
# @Time   :2019/08/14
# @Author    : chenyue

"""
封装Cookie方法
"""
import requests
from CaibeikeAPItest.Common import Log
from CaibeikeAPItest.Config import Config


class Session:
    def __init__(self):
        self.config = Config.Config()
        self.log = Log.MyLog()

    def get_session(self, env):
        """
        获取session
        :param env:环境
        :return:
        """
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (HTML, like Gecko)\
                                  Chrome/67.0.3396.99 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        if env == "PRE_DEBUG":
            login_url = 'http://' + self.config.loginHost_debug
            parm = self.config.loginInfo_debug

            session_debug = requests.session()
            response = session_debug.post(login_url, parm, headers=headers)
            print(response.cookies)
            self.log.debug('cookie:%s' % response.cookies.get_dict())
            return response.cookies.get_dict()
        elif env == "MAPI_DEBUG":
            login_url = 'http://' + self.config.loginHost_release
            parm = self.config.loginInfo_release

            session_release = requests.session()
            response = session_release.post(login_url, parm, headers=headers)
            print(response.cookies)
            self.log.debug('cookie:%s' % response.cookies.get_dict)
            return response.cookies.get_dict()
        else:
            print("get cookie error")
            self.log.error('get cookie error,please check out!!!')


if __name__ == '__main__':
    ss = Session()
    ss.get_session('debug')




