import requests
from datetime import datetime
from pyquery import PyQuery as pq

from ads.db import RedisClient

class DouyuInspector(object):

    def __init__(self, **kwargs):
        self._db_name = 'douyutv'
        self._seed_url = kwargs["seed_url"]
        self._payload = kwargs["payload"]
        self._conn = RedisClient()
    def inspect(self):
        html = requests.get(url=self._seed_url, params=self._payload).text
        doc = pq(html)
        items = doc('li').items()
        for item in items:
            room = {
                'r_url' : 'https://www.douyu.com{}'.format(item.find('a.play-list-link').attr('href')),
                'r_classification' : item.find('div.mes-tit > span.ellipsis').text(),
                "time": datetime.today().strftime("%Y-%m-%d %H:%M:%S")
            }
            print(room)
            self._conn.push(self._db_name, room)

if __name__ == '__main__':
    d = DouyuInspector(seed_url='https://www.douyu.com/directory/columnRoom/game',
                       payload={'page' : 1, 'isAjax' : 1})
    d.inspect()