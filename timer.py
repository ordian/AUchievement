# coding=utf-8
import time

def timer(f):
    def wrapper(*args, **kwargs):
        t = time.time()
        result = f(*args, **kwargs)
        print "Время выполнения функции %s: %f" % (f.__name__, (time.time() - t))
        return result
    return wrapper