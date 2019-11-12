# -*- coding: utf-8 -*-
# @Time   :2019/08/21
# @Author    : chenyue

"""
封装requests
"""
import os
import random
import requests
from Common import Session
from Common import Consts
from requests_toolbelt import MultipartEncoder


class Request:
    def __init__(self, env):
        self.session = Session.Session()
        self.get_session = self.session.get_token(env)

    @staticmethod
    def get_request(url, datas, headers):
        """
        封装GET请求
        :param url:
        :param datas:
        :param headers:
        :return:
        """
        if not url.startswith('http://'):
            url = '%s%s' % ('http://', url)
            print(url)
        try:
            if data is None:
                response = requests.get(url=url, headers=headers)
            else:
                response = requests.get(url=url, params=datas, headers=headers)
        except requests.RequestException as e:
            print('%s%s' % ('RequestException url', url))
            print(e)
            return ()
        time_consuming = response.elapsed.microseconds/1000
        time_total = response.elapsed.total_seconds()

        Consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ""
        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts

    @staticmethod
    def post_request(url, data, header):
        """
        封装POST请求
        :param url:
        :param data:
        :param header:
        :return:
        """
        if not url.startswith('http://'):
            url = '%s%s' % ('http://', url)
            print(url)
        try:
            if data is None:
                response = requests.post(url=url, headers=header)
            else:
                response = requests.post(url=url, data=data, headers=header)
        except requests.RequestException as e:
            print('%s%s' % ('RequestException url', url))
            print(e)
            return ()
        except Exception as e:
            print('%s%s' % ('Exception url:', url))
            print(e)
            return ()
        time_consuming = response.elapsed.microseconds/1000
        time_total = response.elapsed.total_seconds()

        Consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''
        response_dicts['text'] = response.text
        response_dicts['time_consuming'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts

    def put_request(self, url, data, header):
        """
        封装put请求
        :param url:
        :param data:
        :param header:
        :return:
        """
        if not url.startswith('http://'):
            url = '%s%s' % ('http://', url)
            print(url)
        try:
            if data is None:
                response = requests.put(url=url, header=header, cookies=self.get_session)
            else:
                response = requests.put(url=url, data=data, header=header, cookies=self.get_session)
        except requests.RequestException as e:
            print("%s%s" % ('RequestException url:', url))
            print(e)
            return ()
        except Exception as e:
            print("%s%s" % ('Exception url:', url))
            print(e)
            return ()

        time_consuming = response.elapsed.microseconds/1000
        time_total = response.elapsed.total_seconds()

        Consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''
        response_dicts['text'] = response.text
        response_dicts['time_coumsing'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts

    def post_request_multipart(self, url, data, header, file_parm, file, f_type):
        """
        提交Multipart/form-data格式的post请求
        :param url:
        :param data:
        :param header:
        :param file_parm:
        :param file:
        :param f_type:
        :return:
        """
        if not url.startswith('http://'):
            url = '%s%s' % ('http://', url)
            print(url)
        try:
            if data is None:
                response = requests.post(url=url,header=header,cookie=self.get_session)
            else:
                data[file_parm] = os.path.basename(file),open(file, 'rb'),f_type
                enc = MultipartEncoder(
                    fields=data,
                    boundary='--------------------' + str(random.randint(1e28,1e29-1))
                )
                header['Content-type'] = enc.content_type
                response = requests.post(url=url, params=data, header=header,cookie=self.get_session)
        except requests.RequestException as e:
            print('%s%s' % ('requests.RequestException URL:', url))
            print(e)
            return ()
        except Exception as e:
            print('%s%s' % ('Exception url', url))
            print(e)
            return ()
        time_consuming = response.elapsed.microseconds/1000
        time_total = response.elapsed.total_seconds()

        Consts.STRESS_LIST.append(time_consuming)

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            response_dicts['body'] = ''

        response_dicts['text'] = response.text
        response_dicts['time_coumsing'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts


if __name__ == '__main__':
    a = Request("PRE_DEBUG")
    URL = 'http://mapi.caibeike.net/index/v4/recommend.html'
    data = {
        "groupId": "1573541951000",
        "start": 0,
        "limit": 10,
        "viewType": "recommend",
        "cityId": "5448b9fa7996edbc1d249fbc"
    }
    header = {
        "Accept-Encoding": "gzip",
        "User-Agent": "Caibeike/1.0(com.caibeike.android 4.3.3; Mi_Note_3;Android 9; f0a34fad7cf8d390; zh_CN)",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "x-app-lat": "31.210729",
        "x-app-lng": "121.4143",
        "x-app-nonce": "4151884388",
        "x-app-platform": "android",
        "x-app-pushid": "170976fa8ace33aced1",
        "x-app-session": "1573541951000",
        "x-app-timestamp": "1573541951000",
        "x-app-token": a.get_session,
        "x-app-uuid": "f0a34fad7cf8d390",
        "x-app-version": "4.3.6"
    }
    aa = Request.post_request(url=URL, datas=data, headers=header)
    print(aa['code'])
    # print(aa['body']['data']['resultList']['result'][0])














