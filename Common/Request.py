# -*- coding: utf-8 -*-
# @Time   :2019/08/12
# @Author    : chenyue

"""
封装requests
"""
import os
import random
import requests
import CaibeikeAPItest.Common.Consts
import CaibeikeAPItest.Common.Session
from requests_toolbelt import multipart

class Request:
    def __init__(self,env):
        self.session = Sess