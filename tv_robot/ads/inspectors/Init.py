# 首先清空当前db的list
from ads.db import RedisClient
conn = RedisClient()

class InspectorInit(object):
    def init(self):
        conn.flush()

if __name__ == '__main__':
    i = InspectorInit()
    i.init()