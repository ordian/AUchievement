# coding=utf-8
studentList = [{'surname': u'Аманов', 'name': u'Карим'},
               {'surname': u'Атамась', 'name': u'Семен'},
               {'surname': u'Афанасьев', 'name': u'Антон'},
               {'surname': u'Бубнов', 'name': u'Никита'},
               {'surname': u'Бугаев', 'name': u'Богдан'},
               {'surname': u'Ворончихин', 'name': u'Станислав'},
               {'surname': u'Жарков', 'name': u'Денис'},
               {'surname': u'Калакуцкий', 'name': u'Аркадий'},
               {'surname': u'Карташов', 'name': u'Никита'},
               {'surname': u'Коваленко', 'name': u'Владимир'},
               {'surname': u'Комаров', 'name': u'Александр'},
               {'surname': u'Крыщенко', 'name': u'Антон'},
               {'surname': u'Лучихин', 'name': u'Кирилл'},
               {'surname': u'Михайленко', 'name': u'Дмитрий'},
               {'surname': u'Моисеева', 'name': u'Анастасия'},
               {'surname': u'Новокрещенов', 'name': u'Константин'},
               {'surname': u'Обедин', 'name': u'Николай'},
               {'surname': u'Овчинников', 'name': u'Даниил'},
               {'surname': u'Ордиян', 'name': u'Андроник'},
               {'surname': u'Разметов', 'name': u'Сергей'},
               {'surname': u'Тураев', 'name': u'Марат'},
               {'surname': u'Тураев', 'name': u'Тимур'},
               {'surname': u'Устюжанина', 'name': u'Екатерина'},
               {'surname': u'Фетцер', 'name': u'Юрий'},
               {'surname': u'Хабибуллин', 'name': u'Марат'},
               {'surname': u'Цветков', 'name': u'Алексей'},
               {'surname': u'Авдеев', 'name': u'Павел'},
               {'surname': u'Бондарев', 'name': u'Тимофей'},
               {'surname': u'Гайдай', 'name': u'Игорь'},
               {'surname': u'Демидов', 'name': u'Герман'},
               {'surname': u'Лиознова', 'name': u'Анна'},
               {'surname': u'Малыгина', 'name': u'Татьяна'},
               {'surname': u'Мелешко', 'name': u'Дмитрий'},
               {'surname': u'Сидоров', 'name': u'Святослав'},
               {'surname': u'Ситдыкова', 'name': u'Надия'},
               {'surname': u'Смолина', 'name': u'Ирина'},
               {'surname': u'Старостина', 'name': u'Екатерина'},
               {'surname': u'Яснев', 'name': u'Олег'}]

courseList = [{'code': 'GT', 'subject': u"Теория графов"},
              {'code': 'CO', 'subject': u"Комбинаторика"},
              {'code': 'AS', 'subject': u"Алгебраические структуры"},
              {'code': 'AL1SE', 'subject': u"Алгоритмы - SE"},
              {'code': 'AL1BI', 'subject': u"Алгоритмы - BI"},
              {'code': 'AL2', 'subject': u"Алгоритмы"},
              {'code': 'ML1', 'subject': u"Математическая логика"},
              {'code': 'ML2', 'subject': u"Математическая логика"},
              {'code': 'UX', 'subject': u"Unix и скриптовые языки"}]

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Web.Web.settings")

from Web.Achievement.views import addCourses
from Web.Achievement.views import addStudents
from django.db import connection

addStudents(studentList)
addCourses(courseList)

cursor = connection.cursor()
with open('sql.commands', 'r') as command_file:
    for command in command_file.readlines():
        cursor.execute(command)
