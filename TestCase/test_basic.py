# -*- coding: utf-8 -*-
# @Time   :2019/08/30
# @Author    : chenyue

import allure
import pytest
from CaibeikeAPItest.Params import params
from CaibeikeAPItest.Config import Config
from CaibeikeAPItest.Common import Request,Consts,Assest


class TestBasic:
    @pytest.allure.feature('Home')
    @allure.severity('blocker')
    @allure.story('Basic')
    def test_basic_01(self, action):
        """
        用例描述：未登录状态下查看基础设置
        :param action:
        :return:
        """

