#! /usr/bin/env python
# -*- coding: utf-8 -*-


from MetaParser import *


def parse(fileOpenXML, time, studentList):
    subject = u"Математическая логика"
    skip = 2
    stop = 23
    getname = lambda row:  (row[2].value, row[3].value)
    leftborder = 5
    rightborder = -8
    convert = to_float
    header = lambda sheet, task: sheet.rows[1][task + 6].value
    metaparse(fileOpenXML, subject, skip, stop, getname, 
              leftborder, rightborder, convert, header, time, studentList, 0, -1)
   
