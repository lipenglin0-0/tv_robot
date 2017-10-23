from CookiesPool.generator.Generator import CookiesGenerator
from CookiesPool.Config import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class QuanminTVCookieGenerator(CookiesGenerator):
    def __init__(self, name = 'quanmintv', browser_type = DEFAULT_BROWSER):
        CookiesGenerator.__init__(self, name = name, browser_type = browser_type)
        self._name = name

    def new_cookies(self, username, password):
        print('Generating Cookies of', username)
        self._browser.delete_all_cookies()
        self._browser.get('https://www.quanmin.tv/category/')
        wait = WebDriverWait(self._browser, 10)
        # 登陆
        login_button = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#main_header > div > div > div.common_w-header_login > div > div.common_w-login_unlogin > span.js-login')
            )
        )
        login_button.click()
        input_text = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '.common_w-login_pannel_name input')
            )
        )
        input_text.send_keys(username)
        input_password = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, '.common_w-login_pannel_password input')
            )
        )
        input_password.send_keys(password)
        input('手动处理验证码之后按回车 ->')
        try:
            submit_button = wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, 'body > div.common_w-dialog.animated.fadeInDown > div.common_w-dialog_wrap > div > div > div.common_w-dialog_content > div > div > div.common_w-tabs_content-wrapper > div.common_w-login_pannel.clearfix > div.common_w-login_pannel_login-btn.qmtv-ui-button')
                )
            )
            submit_button.click()
        except:
            pass

        input('确定登陆成功后，按回车键 ->')
        return self.save_cookies(username)


if __name__ == '__main__':
    qm = QuanminTVCookieGenerator()
    qm.run()

