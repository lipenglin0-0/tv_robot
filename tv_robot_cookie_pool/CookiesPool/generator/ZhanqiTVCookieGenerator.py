from CookiesPool.generator.Generator import CookiesGenerator
from CookiesPool.Config import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class ZhanqiTVCookieGenerator(CookiesGenerator):
    def __init__(self, name = 'zhanqitv', browser_type = DEFAULT_BROWSER):
        CookiesGenerator.__init__(self, name = name, browser_type = browser_type)
        self._name = name

    def new_cookies(self, username, password):
        print('Generating Cookies of', username)
        self._browser.delete_all_cookies()
        self._browser.get('https://www.zhanqi.tv/games')
        wait = WebDriverWait(self._browser, 10)
        #
        login_button = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,
                 '#js-left-panel-more > div.login-content.js-login-area > div.no-login > div > a.login-fn-btn.js-login-btn')
            )
        )
        login_button.click()

        # 登陆button 不好使，手动登录
        print('手动登录->')

        # input_text = wait.until(
        #     EC.presence_of_element_located(
        #         (By.CSS_SELECTOR, '#yp-box-form > div:nth-child(1) > div > input')
        #     )
        # )
        # input_text.send_keys(username)
        # input_password = wait.until(
        #     EC.presence_of_element_located(
        #         (By.CSS_SELECTOR, '#yp-box-form > div:nth-child(2) > div > input')
        #     )
        # )
        # input_password.send_keys(password)
        # submit_button = wait.until(
        #     EC.element_to_be_clickable(
        #         (By.CSS_SELECTOR, '#yp-box-form > div.btn-area > button')
        #     )
        # )
        # submit_button.click()
        # print('如有验证码，请手动处理~')

        input('确定登陆成功后，按回车键~')
        return self.save_cookies(username)


if __name__ == '__main__':
    dy = ZhanqiTVCookieGenerator()
    dy.run()

