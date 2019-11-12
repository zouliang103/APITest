# -*- coding: utf-8 -*-
# @Time   :2019/08/30
# @Author    : chenyue

"""
定义测试数据
"""
import os
from Params import tools
from Common import Log
import time
log = Log.MyLog()
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


def get_parameter(name):
    data = tools.GetPages().get_page_list()
    param = data[name]
    return param


class GetParam:
    log.info('解析yaml from path:' + path_dir)

    @staticmethod
    def get_url(name):
        params = get_parameter(name)
        url = []
        for i in range(0, len(params)):
            url.append(params[i]['url'])
        return url

    @staticmethod
    def get_data(name):
        params = get_parameter(name)
        data = []
        for i in range(0, len(params)):
            data.append(params[i]['data'])
        return data

    @staticmethod
    def get_header(name):
        params = get_parameter(name)
        header = []
        for i in range(0,len(params)):
            header.append(params[i]['header'])
        return header

    @staticmethod
    def new_report_name():
        now = time.strftime('%Y{y}%m{m}%d{d} %H{h}%M{f}%S{s}').format(y='年', m='月', d='日',h='时',f='分',s='秒')
        reports_name =now + '接口自动化测试报告'
        new_report_name = reports_name.replace(" ","")
        return new_report_name
# class Basic:
#     log.info('解析yaml,path:' + path_dir + '\\Params\\Param\\Basic.yaml')
#     params = get_parameter('Basic1')
#     url = []
#     data = []
#     header = []
#     for i in range(0, len(params)):
#         url.append(params[i]['url'])
#         data.append(params[i]['data'])
#         header.append(params[i]['header'])


if __name__ == "__main__":
    dataList = GetParam()
    datas = dataList.get_data("Basic")
    headers = dataList.get_header("Basic")
    urls = dataList.get_url("Basic")
    report_name = dataList.new_report_name()
    cmd = 'pytest --html=../Reports/%s.html --self-contained-html' % report_name
    print(cmd)
    # print(datas)
    # print(headers)
    # print(urls)
