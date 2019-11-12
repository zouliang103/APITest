import time
from Common import Log
from Config import Config, ConnMongoDb
import random
import datetime


class Headers:
    def __init__(self):
        self.config = Config.Config()
        self.log = Log.MyLog()
        self.conn = ConnMongoDb.ConnMongoDb()

    @staticmethod
    def get_timestamp(passtime):
        # 获取当前的时间戳 passtime = 0
        # 获取未来几秒钟的时间戳 passtime = 正数
        # 获取过去时间的时间戳  passtime = 负数
        time_now_add_passtime = (datetime.datetime.now() + datetime.timedelta(seconds=passtime)).strftime\
            ("%Y-%m-%d %H:%M:%S")
        format_time = time.strptime(time_now_add_passtime, "%Y-%m-%d %H:%M:%S")
        time_stamp = int(time.mktime(format_time))
        millisecond_time_stamp = int(round(time_stamp * 1000))
        return str(millisecond_time_stamp)

    @staticmethod
    def get_app_timestamp(timestamp):
        itime = int(timestamp)/1000
        ltime = time.localtime(itime)
        timeYMD = time.strftime("%Y-%m-%d %H:%M:%S", ltime)
        new_time = timeYMD + str(2)
        return new_time

    def get_app_version(self, env):
        version = ''
        if env == "PRE_DEBUG":
            version = self.config.versionCode_debug
        elif env == "MAPI_DEBUG":
            version = self.config.versionCode_release
        else:
            # print("get app version error")
            self.log.error('get app version error,please check out!!!')
        return version

    @staticmethod
    def get_app_nonce():
        nonce = random.randint(0000000000, 9999999999)
        return str(nonce)

    def get_app_cityid(self, city_name):
        myclient = self.conn.client_mongodb()
        dblist = myclient.list_database_names()
        if city_name in dblist:
            print("%s数据库已存在" % city_name)
        else:
            print("数据库")
        myclient.close()
        return "数据库已存在"

    def get_accept_encoding(self,accept_encoding):
        if accept_encoding == "Accept-Encoding":
            self.log.debug('Accept-Encoding:%s' % "gzip")
            return "gzip"
        else:
            print("get Accept-Encoding error")
            self.log.error('get Accept-Encoding error,please check out!!!')


if __name__ == "__main__":
    # header_session = Headers.get_header_session()
    AV = Headers()
    # app_version = AV.get_app_version("PRE_DEBUG")
    # app_nonce = Headers.get_app_nonce()
    # print(header_session, app_version, app_nonce)
    # cityid = AV.get_app_cityid("yapi")
    a = AV.get_timestamp(20)
    aa = AV.get_timestamp(-100)
    print(aa)



