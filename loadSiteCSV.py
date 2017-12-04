# Full path and name to csv file 
csv_filepathname="data/site.csv" 
# Full path to your django project directory 
djangoproject_home="/home/bluedevilresistome/bdrsite/bdrsite" 
import sys,os 
sys.path.append(djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings' 

import django
django.setup()

from database.models import Site 
import csv 

dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"') 

for row in dataReader: 
	if row[0] != 'Site ID': # Ignore the header row, import everything else 
		site = Site()
		site.site_id = row[0]
		site.name = row[1]
		site.save()