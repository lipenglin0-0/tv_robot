'''
1. 启动inspector
2. 启动admin
3. 启动fans
4. **人为注册账号**验证码**
'''
from multiprocessing import Process

from ads.inspectors.PandaInspector import PandaInspector
from ads.inspectors.DouyuInspector import DouyuInspector
from ads.inspectors.HuyaInspector import HuyaInspector
from ads.inspectors.QuanminInspector import QuanminInspector
from ads.inspectors.ZhanqiInspector import ZhanqiInspector
from ads.inspectors.Init import InspectorInit
from ads.fans.Fans import Fans


class Schedule(object):
    def __init__(self):
        pass

    @staticmethod
    def fans_hot(**kwargs):
        fans = Fans()
        print("fans_hot beginning...")
        words = ['six six six!'] # 从本地文件中读取
        fans.jump_channels(words=words)

    @staticmethod
    def inspector_hot(**kwargs):
        print("inspector_hot beginning...")
        i_init = InspectorInit()
        i_init.init()

        inspectors = []
        i_panda = target = PandaInspector(seed_url="http://www.panda.tv/ajax_sort"
                              , payload={"pageno" : "1", "pagenum": "120", "classification": "lol"})
        inspectors.append(i_panda)

        i_douyu = DouyuInspector(seed_url='https://www.douyu.com/directory/columnRoom/game',
                       payload={'page' : 1, 'isAjax' : 1})
        inspectors.append(i_douyu)

        i_huya = HuyaInspector(seed_url='http://www.huya.com/cache.php',
                       payload={'m' : 'LiveList',
                                'do' : 'getLiveListByPage',
                                'gameId' : '100023',
                                'tagAll' : 0,
                                'page' : '1'
                                })
        inspectors.append(i_huya)

        i_quanmin = QuanminInspector(seed_url='https://www.quanmin.tv/game/lol',
                       payload={'p' : 1})
        inspectors.append(i_quanmin)

        i_zhanqi = ZhanqiInspector(seed_url='https://www.zhanqi.tv/api/static/v2.1/game/live/{}/30/{}.json')
        inspectors.append(i_zhanqi)

        for i in inspectors:
            i.inspect()

    def run(self):
        print("schedule beginning...")
        inspector_process = Process(target=Schedule.inspector_hot())
        inspector_process.start()
        fans_process = Process(target=Schedule.fans_hot())
        fans_process.start()

