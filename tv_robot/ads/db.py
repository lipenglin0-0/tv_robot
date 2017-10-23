import redis

from .config import HOST, PORT, PASSWORD
from .error import PoolEmptyError

class RedisClient(object):
    def __init__(self):
        if PASSWORD:
            self._db = redis.Redis(host=HOST, port=PORT, password=PASSWORD, db=2)
        else:
            self._db = redis.Redis(host=HOST, port=PORT, db=2)
    # push 从右边
    def push(self, list_name, room):
        self._db.rpush(list_name, room)
    # pop 从左边
    def pop(self, list_name, count):
        rooms = self._db.lrange(list_name, 0, count-1)
        self._db.ltrim(list_name, count, -1)
        return rooms

    def queue_len(self, list_name):
        return self._db.llen(list_name)

    # 清空该实例中的所有数据
    def flush(self):
        self._db.flushdb()
