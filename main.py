# coding=utf-8
import logging
#from achiever import achieve
from downloader import download
from parser import parse
from updater import update
import time



if __name__ == "__main__":
    # logging.basicConfig(filename="main.log", format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S', level=logging.DEBUG)
    def do_something(sleep_time):
            print 1

            logging.basicConfig(filename="error.log", format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
            level=logging.ERROR)

            logging.info("--------------------begin downloading----------------------")
            #download()
            logging.info("---------------------end downloading----------------------")


            logging.info("--------------------begin parsing----------------------")
            #list = parse()
            logging.info("---------------------end parsing----------------------")


            logging.info("--------------------begin update----------------------")
            #update(list)
            logging.info("---------------------end update----------------------")

            logging.info("--------------------begin achiever----------------------")
            #achieve()
            logging.info("---------------------end achiever----------------------")

            time.sleep(sleep_time)

    while(True):
        do_something(15)

