#! /usr/bin/env python
# -*- coding: utf-8 -*-

import xlrd
import datetime

# Глобальные переменные - зло!
GRAPH_LIST = [9,6,8]
StInfoList = []

def hw_number_graph(hw):
    """
    Возвращает номер домашнего задания
    из порядкового номера задачи
    """
    accumulator = 0
    counter = 1
    for limit in GRAPH_LIST:
        accumulator += limit
        if hw < accumulator:
            return counter
        counter += 1
    return None

class StInfo(object):
    def __init__(self, name, surname, subject, hw, task, score, date):
        self.name = name
        self.surname = surname
        self.subject = subject
        self.hw = hw
        self.task = task
        self.score = score
        self.date = date

    def __repr__(self):
        print surname, name, subject, 

def to_float(num):
    try:
        a = float(num)
        return a
    except Exception:
        a = None
    return a

def parse_graph(file_graph):
    """
    Добавляет записи StInfo в StInfoList
    """
    global StInfoList, GRAPH_LIST
    rb = xlrd.open_workbook(file_graph)
    sheet = rb.sheet_by_index(0)

    meta = sheet.row_values(0) # column names    
    now = datetime.datetime.now()
    for rownum in range(1, sheet.nrows):
        row = sheet.row_values(rownum)
        surname = row[0]
        name = row[1]
        for hw, score in enumerate(row[3:-2]):
            StInfoList.append(StInfo(name, surname, u"Теория графов", hw_number_graph(int(hw)), meta[hw + 3], to_float(score), now))


