import requests
from datetime import datetime

from ads.db import RedisClient

class ZhanqiInspector(object):

    def __init__(self, **kwargs):
        self._db_name = 'zhanqitv'
        self._seed_url = kwargs["seed_url"]
        self._conn = RedisClient()
    def inspect(self):
        url = self._seed_url.format('6', '1') # lol, page1
        data = requests.get(url).json()
        items = data['data']['rooms']
        for item in items:
            room = {
                'r_url': 'https://www.zhanqi.tv{}'.format(item['url']),
                'r_classification': item['fatherGameName'],
                "time": datetime.today().strftime("%Y-%m-%d %H:%M:%S")
            }
            print(room)
            self._conn.push(self._db_name, room)

if __name__ == '__main__':
    d = ZhanqiInspector(seed_url='https://www.zhanqi.tv/api/static/v2.1/game/live/{}/30/{}.json')
    d.inspect()