#! /usr/bin/env python
# -*- coding: utf-8 -*-


from MetaParser import *


def parse(fileOpenXML, time):
    subject_SE = u"AL1SE"
    subject_BI = u"AL1BI"
    skip = 1
    stop = 16
    getname = lambda row: (row[1].value, row[2].value)
    leftborder = 5
    rightborder = None
    metaparse(fileOpenXML, subject_SE, skip, stop, getname,
              leftborder, rightborder, to_float, time, 0, 1)
    skip = 2
    stop = 14
    metaparse(fileOpenXML, subject_BI, skip, stop, getname,
              leftborder, rightborder, to_float, time, 1)
   
