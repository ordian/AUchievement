import os


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Web.Web.settings")

from django.db import connection

def my_custom_sql():
    cursor = connection.cursor()
    SQL_commands=open('sql.commands','r')
    for command in SQL_commands.readlines():
        cursor.execute(command)
