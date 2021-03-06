# -*- coding: utf-8 -*-

import time
from tomorrow import threads
import os.path
import unittest
from public import HTMLTestRunner
from lib import Utils as  U
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

casepath = "."
ini = U.ConfigIni()
result = ini.get_ini('test_case', 'report_file')


def creat_suite():
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(casepath, pattern='runner*.py', top_level_dir=None)
    for test_suite in discover:
        for casename in test_suite:
            testunit.addTest(casename)
            print casename
    return testunit

now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
tdresult = result + '\\' + day
if not os.path.exists(tdresult):
    os.mkdir(tdresult)
filename = tdresult + "\\" + now + "_result.html"

@threads(5)
def run(testcases):
    fp = file(filename, 'wb+')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u'自动化测试报告', description=u'用例执行情况：')
    runner.run(testcases)

if __name__ == "__main__":
    testcase = creat_suite()
    run(testcase)