#! /usr/bin/env python
# -*- coding: utf-8 -*-


import openpyxl
from StudentInfo import StudentInfo
import parser


def simple_score(cell):
    return int(cell.style.fill.start_color.index == "FF00FF00")


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
            name = name.replace(u'ё', u'е')
            surname = surname.replace(u'ё', u'е')
            for task, score in enumerate(row[1:]):
                try:
                    task_num = int(task) + 1
                    student = StudentInfo(name, surname, subject, task_num, 1, simple_score(score), time)
                    parser.StudentInfoList.append(student)
                except:
                    break # ДЗ кончились
