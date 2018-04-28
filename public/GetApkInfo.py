# -*-coding:utf-8 -*-

import re
from math import floor
import subprocess
import os
import lib.Utils as U
import yaml
import sys
from lib import log
reload(sys)
sys.setdefaultencoding('utf-8')

project_path = os.path.split(os.path.realpath(__file__))[0].strip('\public')


def get_apkpath():
    """
    get test APK path in prjPath

    :return:basename
    """
    apks = os.listdir(project_path)

    if len(apks) > 0:
        for apk in apks:
            basename = os.path.basename(apk)
            if basename.split('.')[-1] == "apk":
                apkpath = '\\'.join([project_path, basename])
                return apkpath


class ApkInfo():

    def __init__(self, apkPath):
        self.apkPath = apkPath
        self.log = log.log()

    def getApkSize(self):
        size = floor(os.path.getsize(self.apkPath) / (1024 * 1000))
        return str(size) + "M"

    def getApkPackage(self):
        p = subprocess.Popen("aapt dump badging %s" % self.apkPath, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        match = re.compile("package: name='(\S+)' versionCode='(\d+)' versionName='(\S+)'").match(output.decode())
        if not match:
            raise Exception("can't get packageinfo")
        packagename = match.group(1)
        versionCode = match.group(2)
        versionName = match.group(3)
        self.log.info('packagename:{}'.format(packagename))
        return packagename

    def getApkName(self):
        p = subprocess.Popen("aapt dump badging %s" % self.apkPath, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        t = output.decode().split()
        for item in t:
            # print(item)
            match = re.compile("application-label:(\S+)").search(item)
            if match is not None:
                return match.group(1)

    def getApkActivity(self):
        p = subprocess.Popen("aapt dump badging %s" % self.apkPath, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             stdin=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        match = re.compile("launchable-activity: name=(\S+)").search(output.decode())
        if match is not None:
            Activity = match.group(1).strip('\'')
            self.log.info('activityname:{}'.format(Activity))
            return Activity

if __name__ == '__main__':
    ini = U.ConfigIni()
    path = ini.get_ini('test_info','info')
    Apk = ApkInfo(get_apkpath())
    package = Apk.getApkPackage()
    activity = Apk.getApkActivity()
    with open(ini.get_ini('test_info', 'info'), 'r') as f:
        print yaml.load(f)[0]