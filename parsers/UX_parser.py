#! /usr/bin/env python
# -*- coding: utf-8 -*-


from MetaParser import *

def deal_with_kuzya(sheet, task):
    """
    Magic
    """
    if task < 13:
        return "Bash {0}".format(task)
    else:
        return "Python {0}".format(int(task) - 12)


def UX_parse(fileOpenXML):
    """
    Not tested yet
    """
    subject = u"Unix и скриптовые языки"
    skip = 5
    stop = 31
    getname = lambda row: (row[1].value, row[2].value)
    leftborder = 10
    rightborder = None
    metaparse(fileOpenXML, subject, skip, stop, getname, 
              leftborder, rightborder, to_float, deal_with_kuzya, now)
   

if __name__ == "__main__":
#    StInfoList = []
#    folder = "OpenXML"
#    ext = "xlsx"#
#
    import datetime
    now = datetime.datetime.now()
#
#    UX_parse("{0}.{1}".format(os.path.join(folder, courses.spreadsheets['UX']), ext))
# 
#    for st in StInfoList: print st
