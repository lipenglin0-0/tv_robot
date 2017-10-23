# redis 相关
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_PASSWORD = ''
# key
REDIS_DOMAIN = '*'
REDIS_NAME = '*'

# 默认使用的浏览器
DEFAULT_BROWSER = 'Chrome'

# 产生器类
'''
待完善：调用对应generator
'''
GENERATOR_DICT = {
    'pandatv' : 'PandaTVCookiesGenerator',
    'douyutv' : 'DouyuTVCookieGenerator',
    'huyatv' : 'HuyaTVCookieGenerator',
    'quanmintv' : 'QuanminTVCookieGenerator',
    'zhanqitv' : 'ZhanqiTVCookieGenerator'
}

# 二维码登录平台name
QR_NAME_LIST = ['douyutv', 'zhanqitv']