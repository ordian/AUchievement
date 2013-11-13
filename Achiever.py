# coding=utf-8

from achievers.full_hw import full_hw_achiever
from achievers.hot_n import hot_n_achiever
from achievers.top_n import top_n_achiever
import courses
from timer import timer


@timer
def achieve():
    solved_count = [x + 10 for x in range(0, 100, 10)]

    for course in courses.spreadsheets.keys():
        print course
        hot_n_achiever(course, solved_count)
        full_hw_achiever(course)
        top_n_achiever(course, 3)