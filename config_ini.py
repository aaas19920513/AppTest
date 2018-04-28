# -*-coding:utf-8-*-
import os
import sys
from lib import Utils as U

project_path = os.path.split(os.path.realpath(__file__))[0]
project_path = project_path.replace('\\', '/')


def config_initialize():
    ini = U.ConfigIni()
    ini.set_ini('test_device', 'device', project_path + '/data/device_info.yaml')
    ini.set_ini('test_info', 'info', project_path + '/data/appium_parameter.yaml')
    ini.set_ini('test_case', 'case_xlsx', project_path + '/data/keyword.xlsx')
    ini.set_ini('test_case', 'report_file', project_path + '/report')
if __name__ == '__main__':
    config_initialize()