import datetime
import os

import courses
from parsers import AL1_parser, AL2_parser, CO_parser, GT_parser, AS_parser, ML1_parser, ML2_parser, UX_parser
from timer import timer


StudentInfoList = []

@timer
def parse():
    time = datetime.datetime.now()

    folder = "OpenXML"
    ext = "xlsx"

    GT_file = "{0}.{1}".format(os.path.join(folder, courses.spreadsheets['GT']), ext)
    CO_file = "{0}.{1}".format(os.path.join(folder, courses.spreadsheets['CO']), ext)
    AS_file = "{0}.{1}".format(os.path.join(folder, courses.spreadsheets['AS']), ext)
    AL1_file = "{0}.{1}".format(os.path.join(folder, courses.spreadsheets['AL1SE']), ext)
    AL2_file = "{0}.{1}".format(os.path.join(folder, courses.spreadsheets['AL2']), ext)
    ML1_file = "{0}.{1}".format(os.path.join(folder, courses.spreadsheets['ML1']), ext)
    ML2_file = "{0}.{1}".format(os.path.join(folder, courses.spreadsheets['ML2']), ext)
    # UX_file = "{0}.{1}".format(os.path.join(folder, courses.spreadsheets['UX']), ext)

    GT_parser.parse(GT_file, time)
    CO_parser.parse(CO_file, time)
    AS_parser.parse(AS_file, time)
    AL1_parser.parse(AL1_file, time)
    AL2_parser.parse(AL2_file, time)
    ML1_parser.parse(ML1_file, time)
    ML2_parser.parse(ML2_file, time)
    # UX_parser.parse(UX_file, time)

    return StudentInfoListS
