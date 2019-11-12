# -*- coding: utf-8 -*-
# @Time   :2019/08/12
# @Author    : chenyue

"""
封装Assert方法
"""
import json
from Common import Consts
from Common import Log


class Assertions:
    def __init__(self):
        self.log = Log.MyLog()

    def assert_code(self, code, expected_code):
        """
        验证返回值的状态码
        :param code: 返回的验证码
        :param expected_code:预期验证码
        :return:
        """
        try:
            assert code == expected_code
            return True

        except:
            self.log.error("statusCode error,expected_code is :%s,statusCode is :%s" % (expected_code,code))
            Consts.RESULT_LIST.append('fail')

            raise   # 引发异常，引发了后面的就不执行

    def assert_body(self, body, body_msg, expected_msg):
        """
        验证返回参数中任意或所有属性的值
        :param body: 返回值
        :param body_msg:返回值的某个字段
        :param expected_msg:返回体中的某个字段的预期值
        :return:
        """
        try:
            msg = body[body_msg]
            assert msg == expected_msg
            return True

        except:
            self.log.error("Response body msg != expected_msg,expected_msg is :%s,body_msg is:%s" % (expected_msg, body_msg))
            Consts.RESULT_LIST.append('fail')

            raise

    def assert_msg_not_null(self,body,body_msg):
        """
        :param body: 返回体
        :param body_msg:返回体的某个字段
        :return:
        """
        try:
            msg = body[body_msg]
            assert msg != None or msg != ''
            return True

        except:
            self.log.error("Response body msg is None,The None body body_msg is:%s" % body_msg)
            Consts.RESULT_LIST.append('fail')

            raise



    def assert_in_text(self, body, expected_msg):
        """
        验证response body中是否包含预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            text = json.dumps(body, ensure_ascii=False)
            # print(text)
            assert expected_msg in text
            return True

        except:
            self.log.error("Response body Does not contain expected_msg, expected_msg is %s" % expected_msg)
            Consts.RESULT_LIST.append('fail')

            raise

    def assert_text(self, body ,expected_msg):
        """
        验证返回参数中是否包含预期字符
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            assert body == expected_msg
            return True

        except:
            self.log.error("Response body != expected_msg, expected_msg is %s, body is %s" % (expected_msg, body))
            Consts.RESULT_LIST.append('fail')

            raise
    def assert_time(self, time, expected_max_time):
        """
        验证接口响应时间小于预期最大响应时间，单位:毫秒
        :param time:
        :param expected_time:
        :return:
        """
        try:
            assert time < expected_max_time
            return True
        except:
            self.log.error("Response time >expected_max_time,expected_time is %s,time is %s" % (expected_max_time,time))
            Consts.RESULT_LIST.append('fail')

            raise

