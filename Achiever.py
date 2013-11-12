# coding=utf-8

from achievers.full_hw import full_hw_achiever
from achievers.hot_n import hot_n_achiever
import courses
from timer import timer


@timer
def achieve():
    for course in courses.spreadsheets.keys():
        for solved_count in range(5, 110, 10):
            print course, solved_count
            hot_n_achiever(solved_count, course)

    for course in courses.spreadsheets.keys():
        full_hw_achiever(course)