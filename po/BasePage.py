# -*-coding:utf-8 -*-
__author__ = 'tuihou'

from selenium.webdriver.support.ui import WebDriverWait
from lib import log
from selenium.webdriver.common.by import By
'''
定义基本操作页面
'''


class Action():

    def __init__(self, driver):
        self.driver = driver
        self.applog = log.log()

    def find_element(self, *loc):
        """
        重写元素定位方法
        :param loc: 
        :return: 
        """
        # return self.driver.find_element(*loc)
        try:
            WebDriverWait(self.driver, 15).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except AttributeError:
            self.applog.error(u"%s找不到元素%s"% (self, loc))

    def find_elements(self, *loc):
        """
        重新封装一组元素定位方法
        :param loc: 
        :return: 
        """
        try:
            if len(self.driver.find_elements(*loc)):
                return self.driver.find_elements(*loc)
        except:
            self.applog.error(u"%s 页面中未能找到 %s 元素" % (self, loc))

    def input(self, tag, loc, text):
        """
        输入text
        :param tag: 
        :param loc: 
        :param text: 
        :return: 
        """
        try:
            ele = self.find_element(tag, loc)
            ele.click()
            ele.clear()
            ele.send_keys(text)
        except AttributeError:
            self.applog.error(u"%s输入出错%s" % (self, text))

    def click(self, tag, loc):
        """
        重新封装按钮点击方法
        :param tag: 
        :param loc: 
        :return: 
        """

        try:
            self.find_element(tag, loc).click()
        except AttributeError:
            self.applog.error(u"点击出错,找不到元素%s" % loc)

    def clicks(self, tag, loc, index):
        """
        重新封装按钮点击方法
        :param tag: 
        :param loc: 
        :return: 
        """

        try:
            eles = self.find_elements(tag, loc)
            for i in eles:

        except AttributeError:
            self.applog.error(u"点击出错,找不到元素%s" % loc)

    def swipe(self, st, sy, ex, ey):
        """
        滑动
        分别为:起始点x,y。结束点x,y。与滑动速度。滑动默认800
        """
        return self.driver.swipe(st, sy, ex, ey, duration=900)

    def get_window_size(self):
        """
        获取屏幕分辨率
        :return: {u'width': 1080, u'height': 1920}
        """
        a = 0
        while a < 6:
            try:
                width = self.driver.get_window_size()['width']
                height = self.driver.get_window_size()['height']
                return width, height
            except Exception as e:
                a += 1
                self.applog.error(e)
                self.applog.error('appium failed to get resolution')

    def swipe_ratio(self, st, sy, ex, ey):
        """

        :param st: 起始点宽
        :param sy: 起始点高
        :param ex: 结束点宽
        :param ey: 结束点高
        :return: 滑动动作
        """
        width, height = self.get_window_size()
        return self.swipe(str(st * width), str(sy * height),
                          str(ex * width), str(ey * height))

    def swipe_left(self):
        """
        左滑屏幕
        """
        try:
            self.swipe_ratio(0.8, 0.5, 0.2, 0.5)
        except AttributeError:
            self.applog.error(u'左滑error')

    def swipe_right(self):
        """
        右滑屏幕
        """
        try:
            self.swipe_ratio(0.2, 0.5, 0.8, 0.5)
        except AttributeError:
            self.applog.error(u'右滑error')

    def swipe_up(self):
        """
        上滑屏幕
        """
        try:
            self.swipe_ratio(0.5, 0.8, 0.5, 0.2)
        except AttributeError:
            self.applog.error(u'上滑error')

    def swipe_down(self):
        """
        下滑屏幕
        """
        try:
            self.swipe_ratio(0.5, 0.2, 0.5, 0.8)
        except AttributeError:
            self.applog.error(u'下滑error')

    def swipe_ways(self, ways):
        if ways.lower() == 'left':
            self.swipe_left()
        elif ways.lower() == 'right':
            self.swipe_right()
        elif ways.lower() == 'up':
            self.swipe_up()
        elif ways.lower() == 'down':
            self.swipe_down()
        else:
            self.applog.error(u'滑动参数输入有误')

    def save_screenshot(self, file_path):
        """

        :param file_path:
        :return: 获取android设备截图
        """
        try:
            return self.driver.save_screenshot(file_path)
        except AttributeError:
            self.applog.error(u'截图error')

    def start_activity(self, package, activity):
        """
        启动activity
        package:包名
        activity:.activity
        """
        return self.driver.start_activity(package, activity)

    def open_notifications(self):
        """
        打开系统通知栏
        """
        return self.driver.open_notifications()

    def is_app_installed(self, package):
        """
        检查是否安装
        package:包名
        """
        return self.driver.is_app_installed(package)

    def install_app(self, path):
        """
        安装应用
        path:安装路径
        """
        return self.driver.install_app(path)

    def remove_app(self, package):
        """
        删除应用
        package:包名
        """
        return self.driver.remove_app(package)

    def shake(self, ):
        """
        摇晃设备
        """
        return self.driver.shake()

    def close_app(self, ):
        """
        关闭当前应用
        """
        return self.driver.close_app()

    def reset_app(self, ):
        """
        重置当前应用
        """
        return self.driver.reset()

    def current_activity(self, ):
        """
        当前应用的activity
        """
        return self.driver.current_activity

    def send_key_event(self, arg):
        """
        操作实体按键
        :return:
        """
        event_list = {'entity_home':3,'entity_back':4,'entity_menu':82,'entity_volume_up':24,'entity_volume_down':25}
        if arg in event_list:
            self.driver.keyevent(int(event_list[arg]))

    def send_keys(self, loc, value, clear_first=True, click_first=True):
        try:
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(value)
        except AttributeError:
            self.applog.error(u"%s找不到元素%s" % (self, loc))

    def verify(self, a, b):
        try:
            if a == b:
                pass

        except AttributeError:
            self.applog.error(u"%s断言出错" %a)

    def toggle_location_services(self):
        """
        开关定位服务
        :return:
        """
        return self.driver.toggle_location_services()

    def action_sign(self, action_name, *args):
        """
        定义带参数的反射函数
        :param action_name: 被调用函数名
        :param args:        被调用函数所需参数
        :return:
        """
        try:
            act = getattr(self, action_name)
            func = act(*args)
            return func
        except AttributeError:
            print u'请检查函数名或者参数是否有误'

    def action(self, action_name):
        """
        不带参数的反射函数
        """
        act = getattr(self, action_name)
        return act()


if __name__ == '__main__':
    from appium import webdriver
    import time

    desired_caps = {

        'platformName': 'Android',

        'deviceName': 'ceb44bd3',

        'platformVersion': '5.0.2',

        'appPackage': 'com.taobao.taobao',

        'appActivity': 'com.taobao.tao.welcome.Welcome',

        'unicodeKeyboard': True,

        'resetKeyboard': True

    }

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    a = Action(driver)
    # 休眠五秒等待页面加载完成

    time.sleep(5)

    driver.find_element_by_id("com.taobao.taobao:id/home_searchedit").click()

    time.sleep(2)
    loc = (By.ID, "com.taobao.taobao:id/searchEdit")
    a.send_keys(loc,'yyketttttt')

