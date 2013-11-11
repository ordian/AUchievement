# coding=utf-8
import os
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
        s = "%s %s %s/%s \t\t %s \t\t%s \t\t %s" % (
            self.name, self.surname, self.hw, self.task, self.score, self.date, self.subject)
        return s.encode("utf-8")


def to_float(num):
    try:
        return float(num)
    except:
        if '+' in unicode(num):
            return 1.0
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


def AL_parse(file, begin_score_column):
    """
    Парсинг файла с оценками по алгоритмам (обе подгруппы)
    @param begin_score_column: номер столбца (с нуля) где начинаются оценки (у двух подгруппы они разные)
    @param file: файл в формате OpenXML
    """

    def build_hw_count(row, start):
        """
        Просматривает выданную строку и заполняет список ALG_LIST - число заданий в каждой домашке
        Заполнение делается в соответствии с правилом: если у новой ячейки есть правая жирная граница, то это конец домашки
        @param row: строка, в которой это правило выполняется
        """
        counter = 0
        for cell in row[start:]:
            style = cell.style.borders.right.border_style
            counter += 1
            if style != 'none':
                ALG_LIST.append(counter)
                counter = 0
        if counter:
            ALG_LIST.append(counter)

    workbook = openpyxl.load_workbook(filename=file)
    for sheet in workbook.worksheets:
        ALG_LIST = [] # число заданий в каждой домашке.
        meta = sheet.rows[0] # column names

        build_hw_count(sheet.rows[0], begin_score_column)

        for row in sheet.rows[1:]:
            if row[0].value is None: continue
            surname, name = row[1].value, row[2].value
            for task, score in enumerate(row[begin_score_column:]):
                task_number = meta[task + begin_score_column].value
                if task_number is None: continue
                student = StInfo(name, surname, u"Алгоритмы",
                                 hw_number(int(task), ALG_LIST),
                                 task_number,
                                 to_float(score.value), now)
                StInfoList.append(student)


def CO_parse(file):
    """
    Парсинг файла с оценками по комбинаторике
    @param file: файл в формате OpenXML
    """

    workbook = openpyxl.load_workbook(filename=file)
    for hw, sheet in enumerate(workbook.worksheets[:-1]):
        meta = sheet.rows[0] # column names
        if hw == 2:
            begin_score_column = 2 # колонка с которой начинаются оценки
            end_score_column = -4 # колонка где заканчиваются оценки
        else:
            begin_score_column = 3
            end_score_column = -1

        for row in sheet.rows[1:]:
            surname, name = row[0].value, row[1].value
            for task, score in enumerate(row[begin_score_column:end_score_column]):
                task_number = meta[task + begin_score_column].value
                if task_number is None: continue
                student = StInfo(name, surname, u"Комбинаторика",
                                 int(hw + 1),
                                 task_number,
                                 to_float(score.value), now)
                StInfoList.append(student)


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

    workbook = openpyxl.load_workbook(filename=file)
    for sheet in workbook.worksheets:
        meta = sheet.rows[0] # column names
        build_hw_count(sheet.rows[0])
        for row in sheet.rows[4:]:
            surname, name = row[1].value.split()
            for hw, score in enumerate(row[3:-8]):
                student = StInfo(name, surname, u"Алгебраические структуры", hw_number(int(hw), AS_LIST),
                                 meta[hw + 3].value,
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
    folder = "OpenXML"
    ext = "xlsx"

    import courses, datetime

    now = datetime.datetime.now()
    GT_parse("{0}.{1}".format(os.path.join(folder, courses.spreadsheets['GT']), ext))
    AS_parse("{0}.{1}".format(os.path.join(folder, courses.spreadsheets['AS']), ext))
    CO_parse("{0}.{1}".format(os.path.join(folder, courses.spreadsheets['CO']), ext))
    AL_parse("{0}.{1}".format(os.path.join(folder, courses.spreadsheets['AL1']), ext), 5)
    AL_parse("{0}.{1}".format(os.path.join(folder, courses.spreadsheets['AL2']), ext), 4)

    for key, st in enumerate(StInfoList):
        print key, st