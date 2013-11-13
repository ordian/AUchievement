#! /usr/bin/env python
# -*- coding: utf-8 -*-

import openpyxl
from StudentInfo import StudentInfo
import parser


def to_float(num):
    try:
        return float(num)
    except:
        if '+' in unicode(num):
            return 1.0
        return 0.0


def metaparse(fileOpenXML, subject, skip, stop, getname, leftborder, rightborder, convert_score, time,
              firstSheet=0, lastSheet=None, hw_number_l=None):
    """
    Парсинг файла
    @param fileOpenXML: файл в формате OpenXML
    @param subject: название предмета
    @param skip: индекс первой строки со студентами SE/BI
    @param stop: 1 + индекс последней строки со студентами SE/BI
    @param getname: функция getname(row) для парсинга имени и фамилии
    @param leftborder: индекс столбца с первой оценкой
    @param rightborder: 1 + индекс столбца с последней оценкой
    @param convert_score: функция convert(score.value) преобразует ячейку с баллом
    @param time: текущее время парсинга
    @param studentList: итоговый список студентов
    @param firstSheet: индекс первой таблицы
    @param lastSheet: 1 + индекс последней таблицы
    """
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

    if not hw_number_l:
        hw_number_l = hw_number

    workbook = openpyxl.load_workbook(filename=fileOpenXML)

    for hw, sheet in enumerate(workbook.worksheets[firstSheet:lastSheet]):
        assert isinstance(sheet, openpyxl.worksheet.Worksheet)
        build_hw_count(sheet.rows[skip])
        for row in sheet.rows[skip:stop]:
            surname, name = getname(row)
            name = name.replace(u'ё', u'е')
            surname = surname.replace(u'ё', u'е')
            header = sheet.rows[0]
            for task, score in enumerate(row[leftborder:rightborder]):
                task_number = header[task + leftborder].value
                if task_number is None: continue

                student = StudentInfo(name, surname, subject, hw_number_l(task, hw + firstSheet), task_number,
                                      convert_score(score.value), time)
                parser.StudentInfoList.append(student)
