from CookiesPool.generator.Generator import CookiesGenerator
from CookiesPool.Config import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

import time

class HuyaTVCookieGenerator(CookiesGenerator):
    def __init__(self, name = 'huyatv', browser_type = DEFAULT_BROWSER):
        CookiesGenerator.__init__(self, name = name, browser_type = browser_type)
        self._name = name

    def new_cookies(self, username, password):
        print('Generating Cookies of', username, password)
        self._browser.delete_all_cookies()
        self._browser.get('http://www.huya.com/g')
        wait = WebDriverWait(self._browser, 10)
        #登陆
        login_button = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#nav-login')
            )
        )
        login_button.click()
        iframe = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '#udbsdk_frm_normal')
            )
        )

        # 进入
        self._browser.switch_to_frame(iframe)
        '''
        # 1.用frame的index来定位，第一个是0
        # 2.用id来定位 driver.switch_to.frame("frame1")
        # 3.用name来定位 driver.switch_to.frame("myframe")
        # 4.用WebElement对象来定位
        '''
        # 回到主窗口
        # self._browser.switch_to_default_content()
        input_text = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '#m_commonLogin .E_acct')
            )
        )
        input_text.send_keys(username)
        input_password = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '#m_commonLogin .E_passwd')
            )
        )
        input_password.send_keys(password)
        submit_button = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#m_commonLogin > div.form_item.form_opra > a.m_button_large.E_login')
            )
        )
        submit_button.click()
        input('确定登陆成功后，按回车键~')
        return self.save_cookies(username)


if __name__ == '__main__':
    dy = HuyaTVCookieGenerator()
    dy.run()
