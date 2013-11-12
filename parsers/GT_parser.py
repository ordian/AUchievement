#! /usr/bin/env python
# -*- coding: utf-8 -*-


from MetaParser import *


def parse(fileOpenXML, time):
    subject = "GT"
    skip = 1
    stop = 39
    getname = lambda row: (row[0].value, row[1].value)
    leftborder = 3
    rightborder = -2
    convert = to_float
    metaparse(fileOpenXML, subject, skip, stop, getname,
              leftborder, rightborder, convert, time)
