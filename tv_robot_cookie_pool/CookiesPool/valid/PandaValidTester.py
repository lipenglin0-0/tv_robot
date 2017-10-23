import json
import requests
from pyquery import PyQuery as pq

from CookiesPool.valid.ValidTester import ValidTester

class PandaValidTester(ValidTester):
    def __init__(self, name = 'pandatv'):
        ValidTester.__init__(self, name=name)

    def test(self, cookies, key):
        try:
            cookies_dict = json.loads(cookies)
            response = requests.get(url='https://www.panda.tv/personal', cookies=cookies_dict)
            if response.status_code == 200:
                doc = pq(response.text)
                title = doc('title').text()
                print('title',title)
                if '个人信息' not in title:
                    self.cookies_db.delete_by_key(key)
                    print('delete cookie...')
        except ConnectionError as e:
            print('error:', e.args)

if __name__ == '__main__':
    tester = PandaValidTester()
    tester.run()