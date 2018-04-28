# -*-coding:utf-8 -*-
__author__ = 'tuihou'
import xlrd


def readtable(filepath, sheetno):
    '''
    :param filepath:
    :param sheetno:
    :return:
    '''
    data = xlrd.open_workbook(filepath)
    table = data.sheets()[sheetno]
    return table


def readxls(filepath, sheetno):
    '''
    :param filepath:
    :param sheetno:
    :return:
    '''
    table = readtable(filepath, sheetno)
    for args in range(1, table.nrows):
        yield table.row_values(args)


def locate(sign, filepath, sheetno=0):
    """
     :param sign:
     :param filepath:
     :param sheetno:
     :return:
     """
    table = readtable(filepath, sheetno)
    for i in range(1, table.nrows):
        if sign in table.row_values(i):
            return table.row_values(i)[1:3]

if __name__ == '__main__':
    filepath = 'D:\\App_ui_20171224\\data\\locate.xlsx'
    a = locate('ele1', filepath)
    b = a[0]
    c = a[1]
    print a
    print b
    print c
