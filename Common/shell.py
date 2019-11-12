# -*- coding: utf-8 -*-
# @Time   :2019/08/30
# @Author    : chenyue

"""
封装执行shell语句方法
"""
import subprocess


class Shell:
    @staticmethod
    def invoke(cmd):
        # 创建一个子进程
        output, errs = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode("utf-8")
        return o
