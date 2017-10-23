import requests
from datetime import datetime

from ads.db import RedisClient

class HuyaInspector(object):

    def __init__(self, **kwargs):
        self._db_name = 'huyatv'
        self._seed_url = kwargs["seed_url"]
        self._payload = kwargs["payload"]
        self._conn = RedisClient()
    def inspect(self):
        data = requests.get(url=self._seed_url, params=self._payload).json()
        items = data['data']['datas']
        for item in items:
            room = {
                'r_url': 'http://www.huya.com/{}'.format(item['privateHost']),
                'r_classification': item['gameFullName'],
                "time": datetime.today().strftime("%Y-%m-%d %H:%M:%S")
            }
            print(room)
            self._conn.push(self._db_name, room)

if __name__ == '__main__':
    # 网络竞技直播 100023
    d = HuyaInspector(seed_url='http://www.huya.com/cache.php',
                       payload={'m' : 'LiveList',
                                'do' : 'getLiveListByPage',
                                'gameId' : '100023',
                                'tagAll' : 0,
                                'page' : '1'
                                })
    d.inspect()