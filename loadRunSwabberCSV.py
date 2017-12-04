# Full path and name to csv file 
csv_filepathname="data/run.csv" 
# Full path to your django project directory 
djangoproject_home="/home/bluedevilresistome/bdrsite/bdrsite" 
import sys,os 
sys.path.append(djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings' 

import django
django.setup()

from database.models import Run, Swabber
import csv 

dataReader = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"') 

for row in dataReader: 
	if row[0] != 'Run ID': # Ignore the header row, import everything else 
		run = Run()
		run.run_id = row[0] 
		run.date = row[1] 
		run.time = row[2] 
		run.conditions = row[3] 
		run.initials = row[4]
		run.save()
		swabber = Swabber()
		swabber.run_id = run
		swabber.swabber = row[5]
		swabber.save()