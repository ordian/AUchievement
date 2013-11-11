#! /usr/bin/env python
# -*- coding: utf-8 -*-


from MetaParser import *

def deal_with_davydov(sign):
    """
    @param sign: + или '+ или None
    @return: 1 или None
    """
    if sign == "+" or sign == "'+":
        return 1
    return None

def AT_DAVYDOV_parse(fileOpenXML):
    subject = u"Алгоритмы"
    skip = 4
    stop = 12
    getname = lambda row: (row[1].value, row[2].value)
    leftborder = 4
    rightborder = None
    header = lambda sheet, task: sheet.rows[0][task + 4].value
    metaparse(fileOpenXML, subject, skip, stop, getname, 
              leftborder, rightborder, deal_with_davydov, header, now, 0, 1)
   

if __name__ == "__main__":
#    StInfoList = []
#    folder = "OpenXML"
#    ext = "xlsx"#
#
    import datetime
    now = datetime.datetime.now()
#
#    AT_DAVYDOV_parse("{0}.{1}".format(os.path.join(folder, courses.spreadsheets['AT_DAVYDOV']), ext))
# 
#    for st in StInfoList: print st
