#! /usr/bin/env python
# -*- coding: utf-8 -*-


from MetaParser import *


def GT_parser(fileOpenXML):
    subject = u"Теория графов"
    skip = 1
    stop = 39
    getname = lambda row: (row[0].value, row[1].value)
    leftborder = 3
    rightborder = -2
    convert = to_float
    header = lambda sheet, task: sheet.rows[0][task + 3].value
    metaparse(fileOpenXML, subject, skip, stop, getname, 
              leftborder, rightborder, convert, header, now)


if __name__ == "__main__":
#    StInfoList = []
#    folder = "OpenXML"
#    ext = "xlsx"#
#
    import datetime
    now = datetime.datetime.now()
#
#    GT_parse("{0}.{1}".format(os.path.join(folder, courses.spreadsheets['GT']), ext))
# 
#    for st in StInfoList: print st
