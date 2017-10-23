import requests
from multiprocessing import Process
from ads.fans.TVFans import TVFans
from ads.config import LABEL
import time

'''
1. 登陆
2. 进入某个房间并发言
'''


class Metaclass(type):
    '''
    __ChannelFunc__ 不同平台
    __ChannelCount__ 平台个数
    '''
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs["__ChannelFunc__"] = []
        for k, v in attrs.items():
            if 'channel_' in k:
                attrs["__ChannelFunc__"].append(k)
                count += 1
        attrs["__ChannelCount__"] = count
        return type.__new__(cls, name, bases, attrs)

class Fans(object, metaclass=Metaclass):

    def jump_channels(self, **kwargs):
        print('jump, beginning...')
        label = LABEL
        eval("self.{}(words={})".format(self.__ChannelFunc__[label], kwargs['words']))
        print("jump，ending...")

    # 熊猫tv
    def channel_pandatv(self, **kwargs):
        # 从词库取
        words = kwargs["words"]
        # 自取cookie, 随机返回一个使用次数最少的cookie
        cookie_list = requests.get(url='http://localhost:5000/pandatv/random').text
        print(cookie_list)
        kwargs = {
            'index_url' : 'http://www.panda.tv/all',
            'cookie' : cookie_list,
            'db_name' : 'pandatv',
            'words' : words,
            'selector_input' : '.room-chat-texta',
            'selector_submit' : '.room-chat-send'
        }
        tv = TVFans(**kwargs)
        tv.login_cookie()
        tv.upsurge()
        print('end...')
        time.sleep(20)
    # 斗鱼
    def channel_douyutv(self, **kwargs):
        words = kwargs["words"]
        cookie_list = requests.get(url='http://localhost:5000/douyutv/random').text
        print(cookie_list)
        kwargs = {
            'index_url': 'https://www.douyu.com/directory',
            'cookie': cookie_list,
            'db_name': 'douyutv',
            'words': words,
            'selector_input' : '.cs-textarea',
            'selector_submit' : '.b-btn'
        }
        tv = TVFans(**kwargs)
        tv.login_cookie()
        tv.upsurge()
        print('end...')
        time.sleep(20)

    # 虎牙
    def channel_huyatv(self, **kwargs):
        words = kwargs["words"]
        cookie_list = requests.get(url='http://localhost:5000/huyatv/random').text
        print(cookie_list)
        kwargs = {
            'index_url': 'http://www.huya.com/l',
            'cookie': cookie_list,
            'db_name': 'huyatv',
            'words': words,
            'selector_input': '#pub_msg_input',
            'selector_submit': '.btn-sendMsg'
        }
        tv = TVFans(**kwargs)
        tv.login_cookie()
        tv.upsurge()
        print('end...')
        time.sleep(20)

    #全民
    def channel_quanmintv(self, **kwargs):
        words = kwargs["words"]
        cookie_list = requests.get(url='http://localhost:5000/quanmintv/random').text
        print(cookie_list)
        kwargs = {
            'index_url': 'https://www.quanmin.tv/category/',
            'cookie': cookie_list,
            'db_name': 'quanmintv',
            'words': words,
            'selector_input': '.room_w-sender_textarea',
            'selector_submit': '.room_w-sender_submit-btn'
        }
        tv = TVFans(**kwargs)
        tv.login_cookie()
        tv.upsurge()
        print('end...')
        time.sleep(20)
    # 战旗
    def channel_zhanqitv(self, **kwargs):
        words = kwargs["words"]
        cookie_list = requests.get(url='http://localhost:5000/zhanqitv/random').text
        print(cookie_list)
        kwargs = {
            'index_url': 'https://www.zhanqi.tv/games',
            'cookie': cookie_list,
            'db_name': 'zhanqitv',
            'words': words,
            'selector_input': '.js-chat-msg-input',
            'selector_submit': '.js-chat-msg-btn'
        }
        tv = TVFans(**kwargs)
        tv.login_cookie()
        tv.upsurge()
        print('end...')
        time.sleep(20)





