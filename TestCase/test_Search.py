import pytest
from Params import params
from Common.Request import Request
from Common.Assest import Assertions
from Common.headers import Headers
from Config.Config import Config
from Common import Consts

config = Config()
Search_data = params.GetParam.get_data('Search')[0]
# /index/v4/recommend 的参数groupId为时间戳
Search_data['groupId'] = Headers.get_timestamp(0)
Search_Url = 'http://' + config.host_debug + params.GetParam.get_url('Search')[0]


class TestRecommendSearch(object):
    def test_recommend_ugc(self, get_request_header):
        """
        查看首页推荐是否有玩法
        :return:
        """
        response = Request.post_request(url=Search_Url, data=Search_data, header=get_request_header)
        assert Assertions().assert_code(response['code'], 200)
        assert response['body']['data']['resultList']['total'] > 0
        assert Assertions().assert_body(response['body'], 'message', 'success')
        Consts.RESULT_LIST.append('true')

    def test_recommend_(self):
        """
        查看首页商品排序是否正确
        :return:
        """
        pass

    def test_feeds_commodity_index(self):
        """
        查看首页feed中是否展示了商品及对应顺序是否正确
        :return:
        """
        pass
