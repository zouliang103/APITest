# -*- coding: utf-8 -*-
# @Time   :2019/08/12
# @Author    : chenyue

"""
封装Log等级及方法
"""
import logging
import os
import time

LEVELS = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARN,
    'error': logging.ERROR,
    'critical': logging.CRITICAL
}
logger = logging.getLogger()   # 构建一个名为logger的日志实例
level = 'default'  # 初始化字段level


def creat_file(filename):
    """
    创建日志文件夹
    """
    path = filename[0:filename.rfind('/')]  # rfind返回字符串最后一次出现的位置
    if not os.path.isdir(path):
        os.makedirs(path)
    if not os.path.isfile(path):
        fd = open(filename, mode='w', encoding='utf-8')
        fd.close()
    else:
        pass


def set_hander(levels):
    """
     设置日志输出的位置
    """
    if levels == 'error':
        logger.addHandler(MyLog.err_hander)
    logger.addHandler(MyLog.hander)


def remove_hander(levels):
    """
    避免重复打印日志
    """
    if levels == 'error':
        logger.removeHandler(MyLog.err_file)
    logger.removeHandler(MyLog.hander)


def get_current_time():
    """
    获取当前时间
    """
    return time.strftime(MyLog.date, time.localtime(time.time()))


class MyLog:
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 获取项目的根目录
    log_file = path + "/Log/log.log"
    err_file = path + "/Log/err.log"
    logger.setLevel(LEVELS.get(level, logging.NOTSET))  # 初始化日志的级别，
    # 如果level在LVELES中返回level，否则返回NOTSET
    creat_file(log_file)
    date = '%Y-%m-%d %H:%M:%S'
    hander = logging.FileHandler(log_file, encoding='utf-8')
    err_hander = logging.FileHandler(err_file, encoding='utf-8')

    @staticmethod
    def debug(log_msg):
        set_hander('debug')
        logger.debug("[DEBUG" + get_current_time() + "]" + log_msg)
        remove_hander('debug')

    @staticmethod
    def info(log_msg):
        set_hander('info')
        logger.debug("[info" + get_current_time() + "]" + log_msg)
        remove_hander('info')

    @staticmethod
    def waring(log_msg):
        set_hander('waring')
        logger.debug("[waring" + get_current_time() + "]" + log_msg)
        remove_hander('waring')

    @staticmethod
    def error(log_msg):
        set_hander('error')
        logger.debug("[ERROR" + get_current_time() + "]" + log_msg)
        remove_hander('error')

    @staticmethod
    def critical(log_msg):
        set_hander('critical')
        logger.debug("[CRITICAL" + get_current_time() + "]" + log_msg)
        remove_hander('critical')


if __name__ == '__main__':
    MyLog.debug('This is a debug message')
    MyLog.info('This is a info message')
    MyLog.waring('This is a waring message')
    MyLog.error('This is a error message')
    MyLog.critical('This is a critical message')


