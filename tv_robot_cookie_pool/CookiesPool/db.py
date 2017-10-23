import redis
import random

from CookiesPool.Config import *
from CookiesPool.error import *

# 一定要注意，这个要db 1，否则会和db 2，直播间地址发生冲突
class RedisClient(object):
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD):
        if password:
            self._db = redis.Redis(host=host, port=port, password=password, db=1)
        else:
            self._db = redis.Redis(host=host, port=port, db=1)
        self._domain = REDIS_DOMAIN
        self._name = REDIS_NAME

    def _key(self, key):
        """
        得到格式化的key
        :param key: 最后一个参数key
        :return:
        """
        return "{domain}:{name}:{key}".format(domain=self._domain, name=self._name, key=key)

    def set(self, key, value):
        """
        设置键值对
        :param key:
        :param value:
        :return:
        """
        raise NotImplementedError

    def get(self, key):
        """
        根据键名获取键值
        :param key:
        :return:
        """
        raise NotImplementedError

    def delete(self, key):
        """
        根据键名删除键值对
        :param key:
        :return:
        """
        raise NotImplementedError

    def keys(self):
        """
        得到所有键名
        :return:
        """
        return self._db.keys('{domain}:{name}:*'.format(domain=self._domain, name=self._name))

    def flush(self):
        """
        清空数据库, 慎用
        :return:
        """
        self._db.flushall()

# domain,name 可默认，可自选
class CookiesRedisClient(RedisClient):
    def __init__(self, host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, domain='cookie', name='default'):
        RedisClient.__init__(self, host=host, port=port, password=password)
        self._domain = domain
        self._name = name

    def set(self, key, value):
        try:
            self._db.set(self._key(key=key), value=value)
        except:
            raise SetCookieError

    def get(self, key):
        print(self._key(key=key))
        try:
            return self._db.get(self._key(key=key)).decode('utf-8')
        except:
            return None

    def get_by_key(self, key):
        print('key:', key)
        try:
            return self._db.get(key).decode('utf-8')
        except:
            return None

    def delete(self, key):
        try:
            print('Delete', key)
            return self._db.delete(self._key(key=key))
        except:
            raise DeleteCookieError
    def delete_by_key(self, key):
        print('key:', key)
        try:
            return self._db.delete(key)
        except:
            raise DeleteCookieError

    def random(self):
        try:
            keys = self.keys()
            return self._db.get(random.choice(keys))
        except:
            raise GetRandomCookieError

    def all(self):
        try:
            for key in self.keys():
                group = key.decode('utf-8').split(':')
                if len(group) == 3:
                    account = group[2]
                    yield {
                        'username': account,
                        'cookies': self.get(account)
                    }
        except:
            raise GetAllCookieError

    def count(self):
        return len(self.keys())

    # 保存cookie加入时间
    # class AcountTimeRedisClient(RedisClient):
    #     def __init__(self):

if __name__ == '__main__':
    crc = CookiesRedisClient(name='pandatv')
    print(crc.keys())