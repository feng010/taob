
class Custom(object):
    def __init__(self, name=''):
        self.name = name
c = Custom('吕小布')

class Seller(object):
    def __init__(self):
        pass
    def work(self,info):
        print('上班打卡')
        print('今天我的工作{}'.format(info))
        print('下班打卡')
s = Seller()

s.work('玩')
