# coding=utf-8
import logging
import sys
import sched
import time

from Achiever import achieve
from downloader import download
from parser import parse
from updater import update


def process(scheduler=None, timer=None):
    # logging.basicConfig(filename="main.log", format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S', level=logging.DEBUG)

    logging.basicConfig(filename="error.log", format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                        level=logging.ERROR)

    logging.info("--------------------begin downloading----------------------")
    download()
    logging.info("---------------------end downloading----------------------")

    logging.info("--------------------begin parsing----------------------")
    list = parse()
    logging.info("---------------------end parsing----------------------")

    logging.info("--------------------begin update----------------------")
    update(list)
    logging.info("---------------------end update----------------------")

    logging.info("--------------------begin achiever----------------------")
    achieve()
    logging.info("---------------------end achiever----------------------")
    if scheduler:
        scheduler.enter(timer, 1, process, (scheduler, timer))


if __name__ == "__main__":
    try:
        timer = int(sys.argv[1])
        scheduler = sched.scheduler(time.time, time.sleep)
        scheduler.enter(timer, 1, process, (scheduler, timer))
        scheduler.run()
    except:
        process()