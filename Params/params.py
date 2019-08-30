# -*- coding: utf-8 -*-
# @Time   :2019/08/30
# @Author    : chenyue

"""
定义测试数据
"""
import os
from CaibeikeAPItest.Params import tools
from CaibeikeAPItest.Common import Log

log = Log.MyLog()
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


def get_parameter(name):
    data = tools.GetPages().get_page_list()
    param = data[name]
    return param


class Basic:
    log.info('解析yaml,path:' + path_dir + 'Params/Yaml/Basic.yaml')
    params = get_parameter('Basic')
    url = []
    data = []
    header = []
    for i in range(0, len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['data'])
