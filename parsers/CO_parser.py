#! /usr/bin/env python
# -*- coding: utf-8 -*-


from MetaParser import *


def CO_parse(fileOpenXML):
    subject = u"Комбинаторика"
    skip = 1
    stop = 39
    getname = lambda row:  (row[0].value, row[1].value)
    leftborder = 3
    rightborder = -1
    convert = to_float
    header = lambda sheet, task: sheet.rows[0][task + 3].value
    metaparse(fileOpenXML, subject, skip, stop, getname, 
              leftborder, rightborder, convert, header, now, 0, 2)
    metaparse(fileOpenXML, subject, skip, stop, getname, 
              2, -4, convert, header, now, 2, 3)
    metaparse(fileOpenXML, subject, skip, stop, getname, 
              leftborder, rightborder, convert, header, now, 3, -1)
  

if __name__ == "__main__":
#    StInfoList = []
#    folder = "OpenXML"
#    ext = "xlsx"#
#
    import datetime
    now = datetime.datetime.now()
#
#    CO_parse("{0}.{1}".format(os.path.join(folder, courses.spreadsheets['CO']), ext))
# 
#    for st in StInfoList: print st
