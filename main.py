# coding=utf-8
import logging
import sys
import time

from achiever import achieve
from downloader import download
from parser import parse
from updater import update


if __name__ == "__main__":
    def process(sleep_time):
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

        time.sleep(sleep_time)


    while True:
        #todo replace to 3600

        if len(sys.argv) < 2:
            process(0)
            break
        else:
            process(int(sys.argv[1]))
