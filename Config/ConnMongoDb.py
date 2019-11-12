from Config import Config
from Common import Log
from sshtunnel import SSHTunnelForwarder
import pymongo


# 利用ssh链接mongodb
class ConnMongoDb:
    def __init__(self):
        self.config = Config.Config()
        self.log = Log.MyLog()

    def client_mongodb(self):
        ecs_host = self.config.md_ssh_add
        ecs_user = self.config.md_ssh_username
        ecs_pwd = self.config.md_ssh_pwd
        mongo_host = self.config.md_host
        mongo_port = int(self.config.md_port)
        mongo_database = self.config.md_database
        mongo_account = self.config.md_username
        mongo_password = self.config.md_password
        server = SSHTunnelForwarder(
            ssh_address_or_host=(ecs_host,22),
            ssh_password=ecs_pwd,
            ssh_username=ecs_user,
            remote_bind_address=(mongo_host, mongo_port))

        # server.start()
        # print(server.local_bind_port)
        uri = "mongodb://%s:%s@%s/%s?authMechanism=MONGODB-CR" % (mongo_account,
                                                                  mongo_password,
                                                                  mongo_host,
                                                                  mongo_database)
        print(uri)
        # client = pymongo.MongoClient(uri)
        # a = client.list_database_names()
        # print(a)
        # client.close()
        # return client


if __name__ == "__main__":
    CM = ConnMongoDb()
    CM.client_mongodb()




