# Full path and name to csv file 
csv_filepathname="data/agar" 
# Full path to your django project directory 
djangoproject_home="/home/bluedevilresistome/bdrsite/bdrsite" 
import sys,os 
sys.path.append(djangoproject_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings' 

import django
django.setup()

from database.models import Run, Agar1Log, Agar2Log, Agar3Log, Agar4Log, Agar5Log, Agar6Log
import csv 

for agarID in range(1,7):
	agarTable = csv.reader(open(csv_filepathname + str(agarID) + "log.csv"), delimiter=',', quotechar='"') 
	klass = globals()["Agar" + str(agarID) + "Log"]
	for row in agarTable:
		if row[0] == 'Run ID' or row[0] is None or len(row[0])==0:
			continue
		else:
			agarlog = klass()
			agarlog.run_id = Run.objects.get(run_id=int(row[0]))
			# print(int(row[0]))
			if(row[1] is not None and len(row[1])!=0): 
				agarlog.site_1 = int(row[1])
			if(row[2] is not None and len(row[2])!=0): 
				agarlog.site_2 = int(row[2])
			if(row[3] is not None and len(row[3])!=0): 
				agarlog.site_3 = int(row[3])
			if(row[4] is not None and len(row[4])!=0): 
				agarlog.site_4 = int(row[4])
			if(row[5] is not None and len(row[5])!=0): 
				agarlog.site_5 = int(row[5])
			if(row[6] is not None and len(row[6])!=0): 
				agarlog.site_6 = int(row[6])
			if(row[7] is not None and len(row[7])!=0): 
				agarlog.site_7 = int(row[7])
			if(row[8] is not None and len(row[8])!=0): 
				agarlog.site_8 = int(row[8])
			if(row[9] is not None and len(row[9])!=0): 
				agarlog.site_9 = int(row[9])
			if(row[10] is not None and len(row[10])!=0): 
				agarlog.site_10 = int(row[10])
			if(row[11] is not None and len(row[11])!=0): 
				agarlog.site_11 = int(row[11])
			if(row[12] is not None and len(row[12])!=0): 
				agarlog.site_12 = int(row[12])
			if(row[13] is not None and len(row[13])!=0): 
				agarlog.site_13 = int(row[13])
			if(row[14] is not None and len(row[14])!=0): 
				agarlog.site_14 = int(row[14])
			if(row[15] is not None and len(row[15])!=0): 
				agarlog.site_15 = int(row[15])
			if(row[16] is not None and len(row[16])!=0): 
				agarlog.site_16 = int(row[16])
			if(row[17] is not None and len(row[17])!=0): 
				agarlog.site_17 = int(row[17])
			agarlog.save()