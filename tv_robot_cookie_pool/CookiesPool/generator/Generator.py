from CookiesPool.db import CookiesRedisClient
from CookiesPool.Config import *
from selenium import webdriver

import json


class CookiesGenerator(object):

    def __init__(self, name='default', browser_type=DEFAULT_BROWSER):
        self._name = name
        self.cookie_db = CookiesRedisClient(name=self._name)
        self._browser_type = browser_type

    def _init_browser(self, browser_type):
        if browser_type == 'Chrome':
            self._browser = webdriver.Chrome()
            self._browser.maximize_window()

    def new_cookies(self, username, password):
        raise NotImplementedError

    def set_cookies(self, acount):
        results = self.new_cookies(acount.get('username'), acount.get('password'))
        if results:
            username, cookies = results
            print('Saving Cookies To Redis', username, cookies)
            self.cookie_db.set(username, cookies)

    def save_cookies(self, username):
        cookies = {}
        for cookie in self._browser.get_cookies():
            cookies[cookie['name']] = cookie['value']
        print('cookie:', cookies)
        return (username, json.dumps(cookies))

    def run(self):
        self._init_browser(browser_type=self._browser_type)
        acount = {
            'username': '',
            'password': '',
        }
        if self._name not in QR_NAME_LIST:
            acount['username'] = input('用户名:')
            acount['password'] = input('密码:')
        else:
            acount['username'] = input('用户名:')

        self.set_cookies(acount=acount)

    def close(self):
        try:
            print('Closing Browser!')
            self._browser.close()
            del self._browser
        except:
            print('Browser Is Not Open!')
