import csv
import os
from webapp.models import Company, Data

from django.db import connection

DIR = './downloads'


def parse_all_files():
    try:
        print('Start parsing . . . ')
        files = os.listdir(path=DIR)
        for f in files:
            file = os.path.relpath(f)
            open_file(os.path.join(DIR, file))
    except FileNotFoundError:
        print(f'No such file or directory: {DIR}')


def open_file(f):
    file = open(f)
    reader = csv.reader(file)
    filename = os.path.basename(f)
    name = os.path.splitext(filename)[0]
    print(name)
    company, create = Company.objects.get_or_create(name=name)
    for row in reader:
        if row[0] == 'Date':
            continue
        print(row)
        data, create = Data.objects.get_or_create(
            company=company,
            date=row[0],
            open=row[1],
            high=row[2],
            low=row[3],
            close=row[4],
            adj_close=row[5],
            volume=row[6]
        )
