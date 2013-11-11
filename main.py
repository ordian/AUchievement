import logging
from downloader import download
from parser import parse


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S', level=logging.DEBUG)
    logging.info("--------------------begin downloading----------------------")
    download()
    logging.info("---------------------end downloading----------------------")

    logging.info("--------------------begin parsing----------------------")
    parse()
    logging.info("---------------------end parsing----------------------")