#! /usr/bin/env python
# -*- coding: utf-8 -*-

from MetaParser import *

#WARNING! NOT TESTED YET
def parse(fileOpenXML, time):
    subject = u"UX"
    skip = 5
    stop = 31
    getname = lambda row: (row[1].value, row[2].value)
    leftborder = 10
    rightborder = None
    convert = to_float
    hw_number_l = lambda task, offset: (task < 12 and "Bash") or (1 and "Python")
    metaparse(fileOpenXML, subject, skip, stop, getname,
              leftborder, rightborder, convert, time, 0, -1, hw_number_l)
   
