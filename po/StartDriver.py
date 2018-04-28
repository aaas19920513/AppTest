# -*-coding:utf-8-*-
from appium import webdriver
from lib import log
from public import StartAppium
from lib import Utils as U
import time
import yaml
from tomorrow import threads

class StartDriver(object):

    def __init__(self, device_l):
        self.device_l = device_l
        self.device = self.device_l['deviceName']
        self.log = log.log()

    def __get_appium_port(self):
        server = StartAppium.Sp(self.device)
        return server.start_appium()

    def start_appium(self):

        number_of_starts = 0
        while number_of_starts < 2:
            try:
                driver = webdriver.Remote(
                    'http://127.0.0.1:%s/wd/hub' %
                    self.__get_appium_port(), self.device_l)
                self.log.info('appium start %s success' % self.device)
                return driver
            except Exception as e:
                number_of_starts += 1
                self.log.error('Failed to start appium :{}'.format(e))
                self.log.error(
                    'Try restarting the appium :{},Trying the {} frequency'.format(self.device, number_of_starts))
                time.sleep(5)
        if number_of_starts > 5:
            self.log.error('Can not start appium, the program exits')
            exit()


def get_device_info():

    device_list = []
    ini = U.ConfigIni()
    test_info = ini.get_ini('test_info', 'info')
    test_device = ini.get_ini('test_device', 'device')
    with open(test_info) as f:
        test_dic = yaml.load(f)[0]
    # appium添加设备后的启动参数
    with open(test_device) as f:
        for device in yaml.load(f):
            device_list.append(dict(test_dic.items() + device.items()))

    return device_list


def main():
    for device_l in get_device_info():
        yield device_l


@threads(5)
def start(device_l):
    d = StartDriver(device_l)
    return d .start_appium()


if __name__ == '__main__':
    a = main()
    for device in a:
        driver = start(device)

