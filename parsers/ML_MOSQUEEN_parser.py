#! /usr/bin/env python
# -*- coding: utf-8 -*-


from MetaParser import *


def ML_MOSQUEEN_parse(fileOpenXML):
    subject = u"Математическая логика"
    skip = 2
    stop = 23
    getname = lambda row:  (row[2].value, row[3].value)
    leftborder = 5
    rightborder = -8
    convert = to_float
    header = lambda sheet, task: sheet.rows[1][task + 6].value
    metaparse(fileOpenXML, subject, skip, stop, getname, 
              leftborder, rightborder, convert, header, now, 0, -1)
   

if __name__ == "__main__":
#    StInfoList = []
#    folder = "OpenXML"
#    ext = "xlsx"#
#
    import datetime
    now = datetime.datetime.now()
#
#    ML_MOSQUEEN_parse("{0}.{1}".format(os.path.join(folder, courses.spreadsheets['ML_MOSQUEEN']), ext))
# 
#    for st in StInfoList: print st
