import json
import requests
from pyquery import PyQuery as pq

from CookiesPool.valid.ValidTester import ValidTester

class HuyaValidTester(ValidTester):
    def __init__(self, name = 'huyatv'):
        ValidTester.__init__(self, name=name)

    def test(self, cookies, key):
        try:
            cookies_dict = json.loads(cookies)
            response = requests.get(url='http://i.huya.com/', cookies=cookies_dict)
            if response.status_code == 200:
                doc = pq(response.text)
                title = doc('h3.header').text()
                print('title',title)
                if '个人中心' not in title:
                    self.cookies_db.delete_by_key(key)
                    print('delete cookie...')
        except ConnectionError as e:
            print('error:', e.args)

if __name__ == '__main__':
    tester = HuyaValidTester()
    tester.run()