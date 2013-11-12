#! /usr/bin/env python
# -*- coding: utf-8 -*-


from MetaParser import *
from StudentInfo import StudentInfo


def simple_score(cell):
    return int(cell.style.fill.start_color.index == "FF00FF00")


def parse(fileOpenXML, time, studentList):
    """
    HARDCORE
    """
    subject = u"Математическая логика"
    workbook = openpyxl.load_workbook(filename=fileOpenXML)
    for sheet in workbook.worksheets:
        assert isinstance(sheet, openpyxl.worksheet.Worksheet)
        for row in sheet.rows[1:]:
            surname, name = row[0].value.split()
            for task, score in enumerate(row[1:8]):
                student = StudentInfo(name, surname, subject, 1 + int(task), 1 + int(task), simple_score(score), time)
                studentList.append(student)