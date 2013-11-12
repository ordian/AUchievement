#! /usr/bin/env python
# -*- coding: utf-8 -*-


from MetaParser import *

def parse(fileOpenXML, time, studentList):
    subject = u"Алгоритмы"
    skip = 4
    stop = 12
    getname = lambda row: (row[1].value, row[2].value)
    leftborder = 4
    rightborder = None
    header = lambda sheet, task: sheet.rows[0][task + 4].value
    metaparse(fileOpenXML, subject, skip, stop, getname, 
              leftborder, rightborder, to_float, header, time, studentList, 0, 1)
   
