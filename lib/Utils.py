# -*- coding: utf-8 -*-

import time
import subprocess
import os
import sys
import ConfigParser


def get_now_time():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))


def sleep(s):
    return time.sleep(s)


def cmd(cmd):
    return subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, bufsize=1, close_fds=False)


class ConfigIni():
    def __init__(self):
        self.current_directory = os.path.split(os.path.realpath(__file__))[0]
        self.path = os.path.split(__file__)[0].replace('lib', 'data/test_info.ini')
        self.cf = ConfigParser.ConfigParser()
        self.cf.read(self.path)

    def get_ini(self, title, value):
        return self.cf.get(title, value)

    def set_ini(self, title, value, text):
        self.cf.set(title, value, text)
        return self.cf.write(open(self.path, "wb"))

    def add_ini(self, title):
        self.cf.add_section(title)
        return self.cf.write(open(self.path))

    def get_options(self, data):
        # 获取所有的section
        options = self.cf.options(data)
        return options

print get_now_time()