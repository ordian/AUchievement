# coding=utf-8
import os
import logging

from apiclient.discovery import build
from apiclient.errors import HttpError
from httplib2 import Http
from oauth2client.client import SignedJwtAssertionCredentials
import sys

import courses


def auth():
    """
    Авторизация и получение доступа к Google Drive
    @return: экземпляр Google Drive
    """
    with open("privatekey.p12", 'rb') as privatekeyFile:
        privatekey = privatekeyFile.read()
    credentials = SignedJwtAssertionCredentials(
        '765315889151-npdj6r2kf8vlsbhdvgoe9ucbig4aeanq@developer.gserviceaccount.com',
        privatekey,
        scope='https://www.googleapis.com/auth/drive')
    return build('drive', 'v2', http=(credentials.authorize(Http())))


def get_file_metadata(service, file_id):
    """
    Получает метаданные файла
    @param service: экземпляр Google Drive
    @param file_id: ID файла (из URL)
    @return: экземпляр метаданных файла
    """
    try:
        return service.files().get(fileId=file_id).execute()
    except Exception as error:
        logging.error("Exception occurred while getting metadata: %s" % error)


def get_openXML_content(service, drive_file):
    """
    Получает контент файла в формате OpenXML
    @param service: экземпляр Google Drive
    @param drive_file: экземпляр метаданных файла, получить можно из метода get_file_metadata
    @return: контент в виде zip архива
    """
    try:
        download_url = drive_file.get('exportLinks')[
            'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet']
        resp, content = service._http.request(download_url)
        if resp.status == 200:
            return content
    except Exception as error:
        logging.error("Exception occurred while downloading file: %s" % error)
        return None


def download():
    """
    Скачивает все документы, перечисленные в файле courses.py в формате OpenXML
    """
    folder_name = "OpenXML"
    try:
        os.stat(folder_name)
    except:
        logging.info("Folder %s doesn't exist, creating folder" % folder_name)
        os.mkdir(folder_name)
    google_drive = auth()
    for course_name, course_file in courses.spreadsheets.items():
        file_metadata = get_file_metadata(google_drive, course_file)
        content = get_openXML_content(google_drive, file_metadata)
        if content is None: continue
        filepath = os.path.join("OpenXML", course_file + ".xlsx")
        with file(filepath, 'wb') as outputFile:
            logging.info("Writing course '%s'..." % course_name)
            outputFile.write(content)


if __name__ == "__main__":
    logging.basicConfig(filename='downloader.log', format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                        level=logging.DEBUG)
    logging.info("--------------------begin downloading----------------------")
    download()
    logging.info("---------------------end downloading----------------------")