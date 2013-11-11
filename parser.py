#! /usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd
import datetime

GRAPH_LIST = [9,6,8]
StInfoList = []

class StInfo(object):
    def __init__(self, name, surname, subject, hw, task, score, date):
        self.name = name
        self.surname = surname
        self.subject = subject
        self.hw = hw
        self.task = task
        self.score = score
        self.date = date

def to_float(num):
    try:
        a = float(num)
        return a
    except Exception:
        a = None
    return a

def parse_graph(file_graph):
    global StInfoList, GRAPH_LIST
    rb = xlrd.open_workbook(file_graph)
    sheet = rb.sheet_by_index(0)
    print sheet.show_grid_lines
    meta = sheet.row_values(0) # column names    
    now = datetime.datetime.now()
    for rownum in range(1, sheet.nrows):
        row = sheet.row_values(rownum)
        surname = row[0]
        name = row[1]
        for hw, score in enumerate(row[3:-2]):
            StInfoList.append(StInfo(name, surname, u"Теория графов", int(hw), to_float(meta[hw + 3]), to_float(score), now))


parse_graph('./content.zip')
for st in StInfoList:
    pass#print st.name, st.surname, st.score, st.hw
