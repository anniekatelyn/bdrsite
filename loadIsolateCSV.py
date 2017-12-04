# Full path and name to csv file 
csv_filepathname="data/isolatelog.csv" 
# Full path to your django project directory 
djangoproject_home="/home/bluedevilresistome/bdrsite/bdrsite" 
import sys,os 
sys.path.append(djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings' 

import django
django.setup()

from database.models import Plate, Site, Run, Agar, Isolate
import csv 

isolateID =  1
isoTable = csv.reader(open(csv_filepathname), delimiter=',', quotechar='"') 
for row in isoTable:
	if row[0] is None or row[0] == "Isolate Tag" or row[0] == "DR#":
		continue
	else:
		runID = Run.objects.get(date=row[1], initials=row[2]).run_id
		agarID = Agar.objects.get(media=str.lower(row[4]), temp=str.lower(row[5]), ctx=str.lower(row[6])).agar_id
		plate = Plate.objects.get(run_id=runID, agar_id=agarID, site_id=row[3])
		isolate = Isolate()
		isolate.iso_id = isolateID
		# print(str(runID) + " " + str(agarID) + " " + str(plate.plate_id) + " " + str(isolateID))
		isolateID+=1
		isolate.plate_id = plate
		isolate.save()
