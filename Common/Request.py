# -*- coding: utf-8 -*-
# @Time   :2019/08/21
# @Author    : chenyue

"""
封装requests
"""
import os
import random
import requests
from CaibeikeAPItest.Common import Session
from CaibeikeAPItest.Common import Consts
from requests_toolbelt import MultipartEncoder


class Request:
    def __init__(self, env):
        self.session = Session.Session()
        self.get_session = self.session.get_session(env)

    def get_request(self, url, data, head):
        """
        封装GET请求
        :param url:
        :param data:
        :param head:
        :return:
        """
        if not url.startswith('http://'):
            url = '%s%s' % ('http://', url)
            print(url)
        try:
            if data is None:
                response = requests.get(url=url, headers=head, cookie=self.get_session)
            else:
                response = requests.get(url=url, params=data, headers=head, cookie=self.get_session)
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
        response_dicts['time_coumsing'] = time_consuming
        response_dicts['time_total'] = time_total

        return response_dicts

    def post_request(self, url, data, header):
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
                response = requests.post(url=url, headers=header, cookie=self.get_session)
            else:
                response = requests.post(url=url, data=data, headers=header, cookie=self.get_session)
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
        response_dicts['time_coumsing'] = time_consuming
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
















