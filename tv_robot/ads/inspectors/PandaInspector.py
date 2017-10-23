import requests

from datetime import datetime
from ads.db import RedisClient
'''
1. 得到所有panda TV正在直播的房间信息
2. 存入redis
************
3. 其他平台的
'''

class PandaInspector(object):

    def __init__(self, **kwargs):
        self._db_name = 'pandatv'
        self._seed_url = kwargs["seed_url"]
        self._payload = kwargs["payload"]
        self._conn = RedisClient()
        self._naughty = ['404055'] # 一些官方频道，直接过滤

    def inspect(self):
        # 注意 i, 从第er页开始
        for i in range(1, 4): # 就要三页
            self._payload["pageno"] = i
            data = requests.get(self._seed_url, self._payload).json()
            items = data["data"]["items"]
            for item in items:
                if item['id'] in self._naughty:
                    continue
                room = {
                    "r_url" : "http://www.panda.tv/{}".format(item["id"]),
                    "r_classification" : item["classification"]["cname"],
                    "time" : datetime.today().strftime("%Y-%m-%d %H:%M:%S"),
                }
                # 保存到redis
                self._conn.push(self._db_name, room)
            print(self._db_name, "[已保存第", i, " 页房间信息！]")

if __name__ == '__main__':
    d = PandaInspector(seed_url="http://www.panda.tv/ajax_sort",
                       payload={"pageno" : "1", "pagenum": "120", "classification": "lol"})
    d.inspect()