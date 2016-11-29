__author__ = 'steffendahnke'

import csv
import goslate
import time
import random
import concurrent.futures


path = r'/Users/steffendahnke/Desktop/'
file = "cvs_produktname_test.txt"

executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
gs = goslate.Goslate(executor=executor)

with open(path + file, newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar=' ')
    for row in spamreader:
        de_row = gs.translate(str(row), 'de')
        print(row, "->", de_row)
        time.sleep(random.randrange(10, 60, 1))