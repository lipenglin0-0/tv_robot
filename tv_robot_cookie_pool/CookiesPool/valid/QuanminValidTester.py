import json
import requests
from pyquery import PyQuery as pq

from CookiesPool.valid.ValidTester import ValidTester

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.common.exceptions import TimeoutException

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
browser = webdriver.Chrome(chrome_options = chrome_options,
                           executable_path='D:\\opt\\chromedriver\\chromedriver')

# browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)

class QuanminValidTester(ValidTester):
    def __init__(self, name = 'quanmintv'):
        ValidTester.__init__(self, name=name)

    def test(self, cookies, key):
        try:
            cookies_dict = json.loads(cookies)
            url = 'https://www.quanmin.tv/category/'
            # browser.maximize_window()
            browser.get(url)
            browser.delete_all_cookies()
            for n, v in cookies_dict.items():
                browser.add_cookie({'name': n, 'value': v})
            browser.get(url)
            try:
                wait.until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, '.common_w-login_sub-icon-center')
                    )
                )
                wait.until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, '.common_w-login_sub-icon-follow')
                    )
                )
                wait.until(
                    EC.presence_of_element_located(
                        (By.CSS_SELECTOR, '.common_w-login_sub-icon-logout')
                    )
                )
                doc = pq(browser.page_source)
                self_center = doc('.common_w-login_sub-icon-center').text()
                my_follow = doc('.common_w-login_sub-icon-follow').text()
                logout = doc('.common_w-login_sub-icon-logout').text()
                print(self_center, my_follow, logout)
                if '个人中心' not in self_center and '我的关注' not in my_follow and '退出' not in logout :
                    self.cookies_db.delete_by_key(key)
                    print('delete cookie...')
            except TimeoutException as e:
                self.cookies_db.delete_by_key(key)
                print('delete cookie...')
        except Exception as e:
            print('error:', e.args)
if __name__ == '__main__':
    tester = QuanminValidTester()
    tester.run()