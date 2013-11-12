#! /usr/bin/env python
# -*- coding: utf-8 -*-


from MetaParser import *


def parse(fileOpenXML, time):
    subject = u"AS"
    skip = 4
    stop = 29
    getname = lambda row: row[1].value.split()
    leftborder = 3
    rightborder = -8
    convert = to_float
    metaparse(fileOpenXML, subject, skip, stop, getname,
              leftborder, rightborder, convert, time)