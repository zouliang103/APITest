import pytest
from Common import Session
from Params import params
from Common import headers


@pytest.fixture(scope='class')
def get_request_header():
    retry = 3    # 重试次数
    num_of_try = 0  # 重试了多少次
    header_api = headers.Headers()
    session = Session.Session()
    while num_of_try < retry:
        token = session.get_token("PRE_DEBUG")
        if token is None or token == '':
            num_of_try += 1
        else:
            break
    token = session.get_token("PRE_DEBUG")
    header = params.GetParam.get_header("Basic")[0]
    header['Accept-Encoding'] = header_api.get_accept_encoding("Accept-Encoding")
    header['x-app-nonce'] = header_api.get_app_nonce()
    header['x-app-session'] = header_api.get_timestamp(0)
    header['x-app-timestamp'] = header_api.get_timestamp(1)
    header['x-app-version'] = header_api.get_app_version("PRE_DEBUG")
    header['token'] = token
    return header


