#! /usr/bin/env python
# -*- coding: utf-8 -*-

from MetaParser import *

#WARNING! NOT TESTED YET
def parse(fileOpenXML, time):
    subject = u"UX"
    skip = 4
    stop = 29
    getname = lambda row: (row[1].value, row[2].value)
    leftborder = 10
    rightborder = None
    convert = to_float
    hw_number_l = lambda task, offset: (task < 12 and "Bash") or (1 and "Python")
    
    COURSE_LIST = [] # число заданий в каждой домашке

    def hw_number(task, offset=None):
        """
        @param task: порядковый номер задачи
        @return номер домашнего задания в соотв. с COURSE_LIST
        """
        accumulator = 0
        counter = 1
        for limit in COURSE_LIST:
            accumulator += limit
            if task < accumulator:
                return counter
            counter += 1
        return None

    def build_hw_count(row):
        """
        Просматривает выданную строку и заполняет список 
        COURSE_LIST - число заданий в каждой домашке
        Заполнение делается в соответствии с правилом: если 
        у новой ячейки есть правая жирная граница, то это конец домашки
        @param row: строка, в которой это правило выполняется
        """
        counter = 0
        for cell in row[leftborder:rightborder]:
            style = cell.style.borders.right.border_style
            counter += 1
            if style != 'none':
                COURSE_LIST.append(counter)
                counter = 0
        COURSE_LIST.append(counter)

    workbook = openpyxl.load_workbook(filename=fileOpenXML)

    for hw, sheet in enumerate(workbook.worksheets[firstSheet:lastSheet]):
        assert isinstance(sheet, openpyxl.worksheet.Worksheet)
        build_hw_count(sheet.rows[skip])
        for row in sheet.rows[skip:stop]:
            surname, name = getname(row)
            name = name.replace(u'ё', u'е')
            surname = surname.replace(u'ё', u'е')
            header = sheet.rows[header_row]
            for task, score in enumerate(row[leftborder:rightborder]):
                task_number = task % 12

                student = StudentInfo(name, surname, subject, hw_number_l(task, hw + firstSheet), task_number,
                                      convert_score(score.value), time)
                parser.StudentInfoList.append(student)
                
    skip = 30
    stop = 42
    
    for hw, sheet in enumerate(workbook.worksheets[firstSheet:lastSheet]):
        assert isinstance(sheet, openpyxl.worksheet.Worksheet)
        build_hw_count(sheet.rows[skip])
        for row in sheet.rows[skip:stop]:
            surname, name = getname(row)
            name = name.replace(u'ё', u'е')
            surname = surname.replace(u'ё', u'е')
            header = sheet.rows[header_row]
            for task, score in enumerate(row[leftborder:rightborder]):
                task_number = task % 12

                student = StudentInfo(name, surname, subject, hw_number_l(task, hw + firstSheet), task_number,
                                      convert_score(score.value), time)
                parser.StudentInfoList.append(student)
    
