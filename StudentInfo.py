# coding=utf-8

class StudentInfo(object):
    def __init__(self, name, surname, subject, hw, task, score, date):
        """
        Создание класса студента
        @param name: имя
        @param surname: фамилия
        @param subject: предмет
        @param hw: номер домашнего задания
        @param task: номер задачи внутри одной домашки
        @param score: оценка
        @param date: дата выставления (получения = парсинга)
        """
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