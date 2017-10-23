import json
import time
# from selenium.common.exceptions import UnexpectedAlertPresentException # 弹窗
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import  By
from selenium.webdriver.support import expected_conditions as EC
from ads.config import *

from selenium.webdriver.common.alert import Alert

from ads.db import RedisClient


# driver
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# browser = webdriver.Chrome(chrome_options=chrome_options,executable_path='D:\\ProgramData\\Anaconda3\\Scripts\\chromedriver')
# browser = webdriver.Chrome()

class TVFans(object):
    def __init__(self, index_url, db_name, cookie, words, selector_input, selector_submit):
        self._index_url = index_url
        self._db_name = db_name
        self._cookie = cookie
        self._words = words
        self._selector_input = selector_input
        self._selector_submit = selector_submit
        self._browser = webdriver.Chrome()

        self._wait = WebDriverWait(self._browser, 5)
        self._conn = RedisClient()
    def login_cookie(self):
        self._browser.get(self._index_url)
        cookie_dict = json.loads(self._cookie)
        self._browser.delete_all_cookies()
        for n, v in cookie_dict.items():
            self._browser.add_cookie({'name': n, 'value': v})
        self._browser.get(self._index_url)
        self._browser.maximize_window()

    # 打开多个新标签页
    def upsurge(self):
        # 打开cycle个新标签页
        for i in range(WINDOW_CYCLE):
            self._browser.execute_script("window.open()")
            self._browser.switch_to_window(self._browser.window_handles[-1])

        # 每次取出cycle个url，先打开，再发言
        for i in range((self._conn.queue_len(self._db_name) + WINDOW_CYCLE - 1) // WINDOW_CYCLE):  # 向上取整
            index = 1
            for item in self._conn.pop(self._db_name, WINDOW_CYCLE):
                self._browser.switch_to_window(self._browser.window_handles[index])
                index += 1
                # 将bytes转化为str，再转化为dict，再去url
                self._browser.get(eval(item.decode())["r_url"])
                # selenium 禁止alert 弹窗
                # js = 'window.alert = function() { return }'
                # self._browser.execute_script(js)
                Alert(self._browser).dismiss()
            # 发言
            for word in self._words:
                for j in range(WINDOW_CYCLE):
                    try:
                        self._browser.switch_to_window(self._browser.window_handles[j + 1])
                        input = self._wait.until(
                            EC.presence_of_element_located((By.CSS_SELECTOR, self._selector_input))
                        )
                        submit = self._wait.until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, self._selector_submit))
                        )

                        input.send_keys(word)
                        submit.click()
                        time.sleep(1)  # 发言间隔一秒
                        print(word, "...", j)
                    except (TimeoutException, WebDriverException):
                        continue
