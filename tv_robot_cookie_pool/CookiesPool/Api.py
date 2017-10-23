from flask import Flask, g

from CookiesPool.Config import *
from CookiesPool.db import *

app = Flask(__name__)

@app.route('/')
def index():
    return '<h2>Welcome to Cookie Pool System</h2>'

def get_conn():
    '''
    创建对应db属性,返回当前访问的request
    :return: 
    '''
    for name in GENERATOR_DICT:
        print('api name set:', name)
        if not hasattr(g, name):
            setattr(g, name + '_cookies',
                    eval('CookiesRedisClient' + '(name="' + name + '")')) # db 中的class
    return g

@app.route('/<name>/random')
def random(name):
    '''
    返回一个随机的cookie
    :param name: 对应，config中的generator_dict 中的key
    :return: 
    '''
    g = get_conn()
    cookies = getattr(g, name + '_cookies').random() # 调用函数
    return cookies


@app.route('/<name>/count')
def count(name):
    '''
    获取cookie中的个数
    :param name: 
    :return: 
    '''
    g = get_conn() # 将我们需要的方法
    count = getattr(g, name + '_cookies').count()
    return str(count) if isinstance(count, int) else count


if __name__ == '__main__':
    app.run() # 让server 公开被访问 host='0.0.0.0'


