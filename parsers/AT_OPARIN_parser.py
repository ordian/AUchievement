#! /usr/bin/env python
# -*- coding: utf-8 -*-


from MetaParser import *

def deal_with_oparin(sign):
    """
    @param sign: + или '+ или None
    @return: 1 или None
    """
    if sign == "+" or sign == "'+":
        return 1
    return None

def AT_OPARIN_parse(fileOpenXML):
    subject = u"Алгоритмы"
    skip = 1
    stop = 16
    getname = lambda row: (row[1].value, row[2].value)
    leftborder = 5
    rightborder = None
    header = lambda sheet, task: sheet.rows[0][task + 5].value
    metaparse(fileOpenXML, subject, skip, stop, getname, 
              leftborder, rightborder, deal_with_oparin, header, now, 0, 1)
    skip = 2
    stop = 14
    metaparse(fileOpenXML, subject, skip, stop, getname, 
              leftborder, rightborder, deal_with_oparin, header, now, 1)
   

if __name__ == "__main__":
#    StInfoList = []
#    folder = "OpenXML"
#    ext = "xlsx"#
#
    import datetime
    now = datetime.datetime.now()
#
#    AT_OPARIN_parse("{0}.{1}".format(os.path.join(folder, courses.spreadsheets['AT_OPARIN']), ext))
# 
#    for st in StInfoList: print st
