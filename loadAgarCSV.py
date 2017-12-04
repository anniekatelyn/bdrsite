# Full path and name to csv file 
csv_filepathname="data/agar.csv" 
# Full path to your django project directory 
djangoproject_home="/home/bluedevilresistome/bdrsite/bdrsite" 
import sys,os 
sys.path.append(djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings' 

import django
django.setup()

from database.models import Agar 
import csv 

dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"') 

for row in dataReader: 
	if row[0] != 'Agar ID': # Ignore the header row, import everything else 
		agar = Agar()
		agar.agar_id = row[0]
		agar.media = row[1]
		agar.temp = row[2]
		agar.ctx = bool(int(row[3]))
		agar.save()