#! /usr/bin/env python
# -*- coding: utf-8 -*-


from MetaParser import *


def AS_parse(fileOpenXML):
    subject = u"Алгебраические структуры"
    skip = 4
    stop = 29
    getname = lambda row: row[1].value.split()
    leftborder = 3
    rightborder = -8
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
#    AS_parse("{0}.{1}".format(os.path.join(folder, courses.spreadsheets['AS']), ext))
# 
#    for st in StInfoList: print st