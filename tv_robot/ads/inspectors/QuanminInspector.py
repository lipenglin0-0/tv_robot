import requests
from datetime import datetime
from pyquery import PyQuery as pq

from ads.db import RedisClient

class QuanminInspector(object):

    def __init__(self, **kwargs):
        self._db_name = 'quanmintv'
        self._seed_url = kwargs["seed_url"]
        self._payload = kwargs["payload"]
        self._conn = RedisClient()
    def inspect(self):
        html = requests.get(url=self._seed_url, params=self._payload).text
        doc = pq(html)
        items = doc('li.list_w-video').items()
        for item in items:
            room = {
                'r_url' : 'https:{}'.format(item.find('a.common_w-card_href').attr('href')),
                'r_classification' : item.find('a.common_w-card_category').text(),
                "time": datetime.today().strftime("%Y-%m-%d %H:%M:%S")
            }
            print(room)
            self._conn.push(self._db_name, room)

if __name__ == '__main__':
    d = QuanminInspector(seed_url='https://www.quanmin.tv/game/lol',
                       payload={'p' : 1})
    d.inspect()