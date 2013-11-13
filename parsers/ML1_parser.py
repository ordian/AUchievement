#! /usr/bin/env python
# -*- coding: utf-8 -*-


from MetaParser import *


def parse(fileOpenXML, time):
    # WARNING: not tested yet
    subject = u"ML1"
    skip = 2
    stop = 23
    getname = lambda row: (row[2].value, row[3].value)
    leftborder = 5
    rightborder = -5
    convert = to_float
    metaparse(fileOpenXML, subject, skip, stop, getname,
              leftborder, rightborder, convert, time, 0, 1, None, 1)
   
