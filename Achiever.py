# coding=utf-8

from achievers.full_hw import full_hw_achiever
from achievers.hot_n import hot_n_achiever
from achievers.top_n import top_n_achiever
import courses
from timer import timer


@timer
def achieve():
    for course in courses.spreadsheets.keys():
        for solved_count in range(0, 100, 10):
            print course, solved_count + 10
            hot_n_achiever(course, solved_count + 10)
        full_hw_achiever(course)
        top_n_achiever(course, 3)