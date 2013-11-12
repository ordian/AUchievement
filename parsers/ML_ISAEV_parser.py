#! /usr/bin/env python
# -*- coding: utf-8 -*-


from MetaParser import *

def simple_score(cell):
    return int(cell.style.fill.start_color.index == "FF00FF00")


def ML_ISAEV_parse(fileOpenXML):
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
                student = StInfo(name, surname, subject, 1 + int(task), 1 + int(task), simple_score(score), now)
                StInfoList.append(student)


if __name__ == "__main__":
#    StInfoList = []
#    folder = "OpenXML"
#    ext = "xlsx"#
#
    import datetime
    now = datetime.datetime.now()
#
#    ML_ISAEV_parse("{0}.{1}".format(os.path.join(folder, courses.spreadsheets['ML_ISAEV']), ext))
# 
#    for st in StInfoList: print st
