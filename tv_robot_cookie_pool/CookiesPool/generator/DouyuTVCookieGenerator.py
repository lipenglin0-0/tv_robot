from CookiesPool.generator.Generator import CookiesGenerator
from CookiesPool.Config import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class DouyuTVCookieGenerator(CookiesGenerator):
    def __init__(self, name = 'douyutv', browser_type = DEFAULT_BROWSER):
        CookiesGenerator.__init__(self, name = name, browser_type = browser_type)
        self._name = name

    def new_cookies(self, username, password):
        print('Generating Cookies of', username)
        self._browser.delete_all_cookies()
        self._browser.get('https://www.douyu.com/directory') # https://passport.douyu.com/member/login
        wait = WebDriverWait(self._browser, 10)
        #【二维码】
        login_button = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '#header > div > div > div.o-unlogin.fl > a.u-login.fl')
            )
        )
        login_button.click()
        input('确定登陆成功后，按回车键~')
        return self.save_cookies(username)


if __name__ == '__main__':
    dy = DouyuTVCookieGenerator()
    dy.run()

