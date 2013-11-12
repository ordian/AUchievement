#! /usr/bin/env python
# -*- coding: utf-8 -*-


from MetaParser import *


def parse(fileOpenXML, time):
    subject = u"CO"
    skip = 1
    stop = 39
    getname = lambda row: (row[0].value, row[1].value)
    leftborder = 3
    rightborder = -1
    convert = to_float
    hw_number = lambda task, sheet_number: sheet_number + 1

    metaparse(fileOpenXML, subject, skip, stop, getname,
              leftborder, rightborder, convert, time, 0, 2, hw_number)
    metaparse(fileOpenXML, subject, skip, stop, getname,
              2, -4, convert, time, 2, 3, hw_number)
    metaparse(fileOpenXML, subject, skip, stop, getname,
              leftborder, rightborder, convert,  time, 3, -1, hw_number)