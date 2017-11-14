import csv, sys, os

project_dir = "C:/Users/Deltacola/Documents/deqn/delqn/"

sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'delqn.settings'

import django

django.setup()

from blog.models import DeliveryData

data = csv.reader(open("C:/Users/Deltacola/Documents/deqn/delqn/info.csv"), delimiter=',')

for row in data:
    if row[0] != 'company_name':
        deli = DeliveryData()
        deli.company_name = row[0]
        deli.weight = row[1]
        deli.total_length = row[2]
        deli.del_time = row[3]
        deli.start_area = row[4]
        deli.end_area = row[5]
        deli.price = row[6]
        deli.tel_num = row[7]
        deli.save()
