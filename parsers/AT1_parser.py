#! /usr/bin/env python
# -*- coding: utf-8 -*-


from MetaParser import *

def parse(fileOpenXML, time, studentList):
    subject = u"Алгоритмы"
    skip = 1
    stop = 16
    getname = lambda row: (row[1].value, row[2].value)
    leftborder = 5
    rightborder = None
    header = lambda sheet, task: sheet.rows[0][task + 5].value
    metaparse(fileOpenXML, subject, skip, stop, getname, 
              leftborder, rightborder, to_float, header, time, studentList, 0, 1)
    skip = 2
    stop = 14
    metaparse(fileOpenXML, subject, skip, stop, getname, 
              leftborder, rightborder, to_float, header, time, studentList, 1)
   
