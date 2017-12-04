# Full path and name to csv file 
csv_filepathname="data/agar" 
# Full path to your django project directory 
djangoproject_home="/home/bluedevilresistome/bdrsite/bdrsite" 
import sys,os 
sys.path.append(djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings' 

import django
django.setup()

from database.models import Plate, Site, Run, Agar
import csv 

plateID = 1
for agarID in range(1,7):
	agarTable = csv.reader(open(csv_filepathname + str(agarID) + "log.csv"), delimiter=',', quotechar='"') 
	for row in agarTable:
		if row[0] == 'Run ID' or row[0] is None:
			continue
		else:
			for siteID in range(1, Site.objects.count()+1):
				if row[siteID] is None or len(row[siteID]) == 0:
					continue
				else:
					plate = Plate()
					plate.plate_id = plateID
					plateID+=1
					plate.run_id = Run.objects.get(run_id=int(row[0]))
					plate.site_id = Site.objects.get(site_id=siteID)
					plate.agar_id = Agar.objects.get(agar_id=agarID)
					plate.cfu = int(row[siteID])
					plate.save()