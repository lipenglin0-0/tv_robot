from CookiesPool.generator.Generator import CookiesGenerator
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from CookiesPool.Config import *
from selenium.webdriver.common.by import  By

class PandaTVCookiesGenerator(CookiesGenerator):
    def __init__(self, name='pandatv', browser_type=DEFAULT_BROWSER):
        CookiesGenerator.__init__(self, name=name, browser_type=browser_type)
        self._name = name

    def new_cookies(self, username, password):
        print('Generating Cookies of', username)
        self._browser.delete_all_cookies()
        self._browser.get('http://www.panda.tv/all')
        wait = WebDriverWait(self._browser, 10)

        login_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "#side-tools-bar > div > div.sidebar-expand > div.sidebar-userinfo > div > a.sidebar-userinfo-login-btn"))
        )
        login_button.click()
        input_text = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            "#ruc-dialog-container > div.ruc-dialog-wrap.ruc-dialog-new-wrap > div.ruc-dialog-content > div > div.ruc-form-item.ruc-input-box.clearfix > div > input"))
        )
        input_text.send_keys(username)
        input_password = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#ruc-dialog-container > div.ruc-dialog-wrap.ruc-dialog-new-wrap > div.ruc-dialog-content > div > div:nth-child(2) > input"))
        )
        input_password.send_keys(password)
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "#ruc-dialog-container > div.ruc-dialog-wrap.ruc-dialog-new-wrap > div.ruc-dialog-content > div > div.ruc-form-item.button-container.login-button-container"))
        )

        # 获取验证码
        submit.click()
        get_icode = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR , '#ruc-dialog-container > div.ruc-dialog-wrap.ruc-dialog-new-wrap > div.ruc-dialog-content > div > div.ruc-form-item.ruc-input-box.login-voice-verify > a')
            )
        )
        get_icode.click()
        # 验证码
        icode = input('验证码：')
        input_icode = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#ruc-dialog-container > div.ruc-dialog-wrap.ruc-dialog-new-wrap > div.ruc-dialog-content > div > div.ruc-form-item.ruc-input-box.login-voice-verify > input'))
        )
        input_icode.send_keys(icode)
        # 登陆按钮
        submit.click()
        input('确定登陆成功后 按回车健->')
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".sidebar-userinfo-username"))
        )

        # 抛异常，形成一个习惯
        try:
            login_user = self._browser.find_element_by_css_selector('.sidebar-userinfo-username').text
            print(login_user)
            # 登陆成功，保存cookie
            return self.save_cookies(username)
        except NoSuchElementException as e:
            print(e.msg)
            print('未登录~')

if __name__ == '__main__':
    generator = PandaTVCookiesGenerator()
    generator.run()