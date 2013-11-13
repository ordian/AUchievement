#! /usr/bin/env python
# -*- coding: utf-8 -*-


import openpyxl
from StudentInfo import StudentInfo
import parser


def simple_score(cell):
    return int(cell.style.fill.start_color.index == "FF00FF00")

#WARNING: not tested yet
def parse(fileOpenXML, time):
    """
    HARDCORE
    Каждое домашнее задание имеет 1 задачу
    Задача зачтена, если цвет зелёный
    """
    subject = u"ML2"
    workbook = openpyxl.load_workbook(filename=fileOpenXML)
    for sheet in workbook.worksheets:
        assert isinstance(sheet, openpyxl.worksheet.Worksheet)
        for row in sheet.rows[1:]:
            surname, name = row[0].value.split()
            for task, score in enumerate(row[1:8]):
                student = StudentInfo(name, surname, subject, 1 + int(task), 1, simple_score(score), time)
                StudentList.append(student)
