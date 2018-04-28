# coding:utf-8
__author__ = 'tuihou'

import logging
import os
import time


'''
配置日志文件，输出INFO级别以上的日志
'''


class log():

    def __setMSG(self, level, msg):
        today = time.strftime('%Y-%m-%d')
        file_path = os.path.split(os.path.realpath(__file__))[0].replace('\lib', '\log')
        log_path = '\\'.join([file_path, today])
        logger = logging.getLogger()
        # 定义Handler输出到文件和控制台
        fh = logging.FileHandler(log_path)
        ch = logging.StreamHandler()
        # 定义日志输出格式
        formater = logging.Formatter("%(asctime)s %(levelname)s %(message)s' ")
        fh.setFormatter(formater)
        ch.setFormatter(formater)
        # 添加Handler
        logger.addHandler(fh)
        logger.addHandler(ch)
        # 添加日志信息，输出INFO级别的信息
        logger.setLevel(logging.INFO)
        if level == 'debug':
            logger.debug(msg)
        elif level == 'info':
            logger.info(msg)
        elif level == 'warning':
            logger.warning(msg)
        elif level == 'error':
            logger.error(msg)
        # 移除句柄，否则日志会重复输出
        logger.removeHandler(fh)
        logger.removeHandler(ch)
        fh.close()

    def debug(self, msg):
        self.__setMSG('debug', msg)

    def info(self, msg):
        self.__setMSG('info', msg)

    def warning(self, msg):
        self.__setMSG('warning', msg)

    def error(self, msg):
        self.__setMSG('error', msg)

if __name__ == '__main__':
    a = log()
    a.info('11112222')