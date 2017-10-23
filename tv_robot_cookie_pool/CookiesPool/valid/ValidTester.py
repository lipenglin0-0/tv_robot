from CookiesPool.db import CookiesRedisClient

class ValidTester(object):
    def __init__(self, name='default'):
        self.name = name
        self.cookies_db = CookiesRedisClient(name=self.name)

    def test(self, cookies, key):
        raise NotImplementedError

    def run(self):
        keys = self.cookies_db.keys()
        for key in keys:
            cookies = self.cookies_db.get_by_key(key=key)
            self.test(cookies=cookies, key=key)

