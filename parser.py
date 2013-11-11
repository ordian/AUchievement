# coding=utf-8
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


def to_float(num):
    try:
        return float(num)
    except:
        return None


def hw_number(task, course_list):
    """
    Возвращает номер домашнего задания
    из порядкового номера задачи
    """
    accumulator = 0
    counter = 1
    for limit in course_list:
        accumulator += limit
        if task < accumulator:
            return counter
        counter += 1
    return None


def AS_parse(file):
    """
    Парсинг файла с оценками по алгебраическим структурам
    @param file: файл в формате OpenXML
    """

    AS_LIST = []

    def build_hw_count(row):
        """
        Просматривает выданную строку и заполняет список AS_LIST - число заданий в каждой домашке
        Заполнение делается в соответствии с правилом: если у новой ячейки есть правая жирная граница, то это конец домашки
        @param row: строка, в которой это правило выполняется
        """
        counter = 0
        for cell in row[3:-8]:
            style = cell.style.borders.right.border_style
            counter += 1
            if style != 'none':
                AS_LIST.append(counter)
                counter = 0
        AS_LIST.append(counter)
        print AS_LIST

    workbook = openpyxl.load_workbook(filename=file)
    now = datetime.datetime.now()
    for sheet in workbook.worksheets:
        meta = sheet.rows[0] # column names
        build_hw_count(sheet.rows[0])
        for row in sheet.rows[4:]:
            surname, name = row[1].value.split()
            for hw, score in enumerate(row[3:-8]):
                student = StInfo(name, surname, u"Алгебраические структуры", hw_number(int(hw), AS_LIST),
                                 str(int(meta[hw + 3].value)),
                                 to_float(score.value), now)
                StInfoList.append(student)


def GT_parse(file):
    """
    Парсинг файла с оценками по теории графов
    @param file: файл в формате OpenXML
    """

    GRAPH_LIST = [] # число заданий в каждой домашке.

    def build_hw_count(row):
        """
        Просматривает выданную строку и заполняет список GRAPH_LIST - число заданий в каждой домашке
        Заполнение делается в соответствии с правилом: если у новой ячейки есть правая жирная граница, то это конец домашки
        @param row: строка, в которой это правило выполняется
        """
        counter = 0
        for cell in row[3:-2]:
            style = cell.style.borders.right.border_style
            counter += 1
            if style != 'none':
                GRAPH_LIST.append(counter)
                counter = 0


    workbook = openpyxl.load_workbook(filename=file)
    now = datetime.datetime.now()
    for sheet in workbook.worksheets:
        meta = sheet.rows[0] # column names
        build_hw_count(sheet.rows[1])
        for row in sheet.rows[1:]:
            surname, name = row[0].value, row[1].value
            for hw, score in enumerate(row[3:-2]):
                student = StInfo(name, surname, u"Теория графов", hw_number(int(hw), GRAPH_LIST), meta[hw + 3].value,
                                 to_float(score.value), now)
                StInfoList.append(student)


if __name__ == "__main__":
    StInfoList = []
    GT_parse("OpenXML/0AtjSko0XIgLWdFZnSUdnTmhublJ6OWF5V2MybUJ0MHc.xlsx")
    AS_parse("OpenXML/0AhaIVBqbQZzvdElseEVUcGV5QV8tX1RzSnVIdnJoT0E.xlsx")
    for st in StInfoList:
        print st