import csv, sys, os

project_dir = "C:/Users/Deltacola/Documents/deqn/delqn/delqn/"

sys.path.append(project_dir)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django

django.setup()

from blog.models import DeliveryData

data = csv.reader(open("C:/Users/Deltacola/Documents/deqn/delqn/jihachul.csv"), delimiter=',')

for row in data:
    if row[0] != 'company_name':
        deli = DeliveryData()
        deli.company_name = row[0]
        deli.weight = row[1]
        deli.total_length = row[2]
        deli.start_area = row[3]
        deli.end_area = row[4]
        deli.price = row[5]
        deli.save()
