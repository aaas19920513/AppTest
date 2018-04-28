# -*- coding:utf-8 -*-
__author__ = 'tuihou'

from lib.log import log
from BasePage import Action
from public import locate
import unittest
import lib.Utils as U
import StartDriver as ST
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

ini = U.ConfigIni()
filepath = ini.get_ini('test_case', 'case_xlsx')


class RunTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        d = ST.main()
        for device in d:
            cls.driver = ST.start(device)
            cls.driver.implicitly_wait(30)
        cls.log = log()
        cls.log.info('--'*10)
        cls.log.info('Starting')

    def buildStep(self, keyword, tag=None, loc=None, param=None, wish=None):
        key = "\"" + keyword.lower() + "\""
        params = [tag, loc, param, wish]
        param_text = ""
        for index in range(0, len(params)):
            if params[index] == None or params[index] == "":
                continue
            param_text += '"' + params[index] + '",'
        param_text = param_text[0:-1]
        if len(param_text) != 0:
            step = "A.action_sign({},{})".format(key, param_text)
        else:
            step = "A.action_sign({})".format(key)
        return step

    def action(self, *data):
        A = Action(self.driver)
        steps = locate.readxls(filepath, 1)
        k = 4
        for step in steps:
            if step[0] == data[0]:
                desc = step[2]
                key_word, sign, param, wish = step[3], step[4], step[5], step[7]
                if sign != "":
                    ele = locate.locate(sign, filepath, 3)
                    tag, loc = ele[0], ele[1]
                    if key_word.lower() == 'input':
                        param = data[4]
                        step = self.buildStep(key_word, tag, loc, param)
                        self.log.info("{}:{}".format(desc, step))
                        k += 1
                        eval(step)
                    elif key_word.lower() == 'gettext':
                        step = self.buildStep(key_word, tag, loc)
                        text = eval(step)
                        if text == wish:
                            A.action_sign('Screenshot', data[0], 'PASS')
                        else:
                            A.action_sign('Screenshot', data[0], 'FAIL')
                    else:
                        step = self.buildStep(key_word, tag, loc, param)
                        self.log.info("{}:{}".format(desc, step))
                        eval(step)
                else:
                    step = self.buildStep(key_word, param)
                    self.log.info("{}:{}".format(desc, step))
                    eval(step)

    def runTest(self):
        pass

    @staticmethod
    def getTestFunc(*txt):
        def func(self):
            self.action(*txt)
        return func

    @classmethod
    def tearDownClass(cls):
        cls.log.info('Ending')
        cls.log.info('--'*10)
        cls.driver.quit()


def __generateTestCases():
    cases = locate.readxls(filepath, 0)
    for case in cases:
        if case[2] == "Y":
            print "【Run】" + case[1] + "："
            print " + -" * 8
            datas = locate.readxls(filepath, 2)
            for data in datas:
                print data[2].encode()
                if (data[3] == "Y") & (data[0] == case[0]):
                    setattr(RunTest, 'test_{}_{}'.format(str(data[0]), str(data[1])), RunTest.getTestFunc(*data))


__generateTestCases()


if __name__ == "__main__":
    unittest.main(verbosity=2)

