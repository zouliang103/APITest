# -*- coding: utf-8 -*-
# @Time   :2019/08/14
# @Author    : chenyue

"""
封装获取Cookie方法
"""
import requests
from Common import Log, headers
from Config import Config
from Params import params
from urllib import parse
import json


class Session:
    def __init__(self):
        self.config = Config.Config()
        self.log = Log.MyLog()
        self.headerAPI = headers.Headers()

    def get_token(self, env):

        """
        获取token
        :param env:环境
        :return:
        """
        my_header = params.GetParam.get_header('Login')[0]
        my_header['Accept-Encoding'] = self.headerAPI.get_accept_encoding("Accept-Encoding")
        my_header['x-app-nonce'] = self.headerAPI.get_app_nonce()
        my_header['x-app-session'] = self.headerAPI.get_timestamp(0)
        my_header['x-app-timestamp'] = self.headerAPI.get_timestamp(1)
        my_header['x-app-version'] = self.headerAPI.get_app_version("PRE_DEBUG")
        if env == "PRE_DEBUG":
            # session_debug = requests.session()  # 创建一个session对象
            login_url = 'http://' + self.config.host_debug + params.GetParam.get_url('Login')[0]
            parm = self.config.loginInfo_debug
            parm_dict = json.loads(parm)  # 将parm转换为字典类型
            data = parse.urlencode(parm_dict)  # 将输入参数转化为x-www-form-urlencoded 也就是k1=v1&k2=v2形式
            response = requests.post(login_url, headers=my_header, data=data)
            try:
                my_token = response.json()["data"]["token"]
            except Exception as e:
                print(e)
                my_token = ''
            return my_token
        elif env == "MAPI_DEBUG":
            login_url = 'http://' + self.config.host_release + self.config.loginHost_release
            parm = self.config.loginInfo_release

            session_release = requests.session()
            response = session_release.post(login_url, parm, headers=my_header)
            print(response.cookies)
            self.log.debug('cookie:%s' % response.cookies.get_dict)
            # return response.cookies.get_dict()
            return response.json().get('data').get('token')
        else:
            print("get cookie error")
            self.log.error('get cookie error,please check out!!!')


if __name__ == '__main__':
    ss = Session()


