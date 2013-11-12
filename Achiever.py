# coding=utf-8
import time
from achievers.hot_n import hot_n_achiever
import courses


def timer(f):
    def tmp(*args, **kwargs):
        t = time.time()
        res = f(*args, **kwargs)
        print "Время выполнения функции: %f" % (time.time() - t)
        return res

    return tmp


@timer
def achieve():
    for course in courses.spreadsheets.keys():
        for solved_count in range(5, 110, 10):
            print course, solved_count
            hot_n_achiever(solved_count, course)