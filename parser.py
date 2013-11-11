#! /usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import openpyxl


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
        s = "%s %s %s/%s \t\t %s \t\t%s" % (self.name, self.surname, self.hw, self.task, self.score, self.date)
        return s.encode("utf-8")


GRAPH_LIST = [9, 6, 8]


def hw_number(task, XXX_LIST):
    """
    Возвращает номер домашнего задания
    из порядкового номера задачи
    """
    accumulator = 0
    counter = 1
    for limit in XXX_LIST:
        accumulator += limit
        if task < accumulator:
            return counter
        counter += 1
    return None


def to_float(num):
    try:
        return float(num)
    except:
        return None


def parse_graph(file):
    """
    Парсинг файла с оценками по теории графов
    @param file: файл в формате OpenXML
    """
    workbook = openpyxl.load_workbook(filename=file)
    now = datetime.datetime.now()
    for sheet in workbook.worksheets:
        assert isinstance(sheet, openpyxl.worksheet.Worksheet)
        meta = sheet.rows[0] # column names
        print " ".join(unicode(x.value) for x in meta)
        for row in sheet.rows[1:]:
            surname = row[0].value
            name = row[1].value
            for hw, score in enumerate(row[3:-2]):
                student = StInfo(name, surname, u"Теория графов", hw_number(int(hw), GRAPH_LIST), meta[hw + 3].value,
                            to_float(score.value), now)
                StInfoList.append(student)


ALGSTRUCTURES_LIST = [10, 10, 10, 10]

def parse_algstructures(file):
    """
    Парсинг файла с оценками по алгебраическим структурам
    @param file: файл в формате OpenXML
    """
    workbook = openpyxl.load_workbook(filename=file)
    now = datetime.datetime.now()
    for sheet in workbook.worksheets:
        assert isinstance(sheet, openpyxl.worksheet.Worksheet)
        meta = sheet.rows[0] # column names
        for row in sheet.rows[4:]:
            surname, name = row[1].value.split()
            for hw, score in enumerate(row[3:-8]):
                student = StInfo(name, surname, u"Алгебраические структуры", hw_number(int(hw), ALGSTRUCTURES_LIST), str(int(meta[hw + 3].value)),
                            to_float(score.value), now)
                StInfoList.append(student)


if __name__ == "__main__":
    StInfoList = []
    
