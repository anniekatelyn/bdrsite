# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from . import models
from models import Agar, Site, Run, Swabber, Plate, Isolate, Agar1Log, Agar2Log, Agar3Log, Agar4Log, Agar5Log, Agar6Log
import inspect

table_descriptions = {"Agar":"Media, incubation temperature, and presence of an antibiotic for each type of agar that samples were plated with.", "Agar1Log":"Raw data for CFUs of samples plated on agar type 1.", "Agar2Log":"Raw data for CFUs of samples plated on agar type 2.", "Agar3Log":"Raw data for CFUs of samples plated on agar type 3.", "Agar4Log":"Raw data for CFUs of samples plated on agar type 4.",
"Agar5Log":"Raw data for CFUs of samples plated on agar type 5.", "Agar6Log":"Raw data for CFUs of samples plated on agar type 6.", "Isolate":"Data for each isolate (plated samples with interesting or unique growth).","Plate":"For each sample that was plated, provides the plating details and CFU count.","Run":"Data describing each sampling run.","Site":"Sites that were visited on a sampling run.","Swabber":"For each run, the initials of the sampling swabber."}

def index(request):
	# add table names from model
	table_descriptions_local = {}
	for name, obj in inspect.getmembers(models):
		if inspect.isclass(obj):
			table_descriptions_local[obj.__name__] = table_descriptions[obj.__name__]
			# table_names.append(obj.__name__)
	# template = loader.get_template('database/index.html')
	context = {'table_descriptions':table_descriptions_local,}
	# return HttpResponse(template.render(context, request))
	return render(request, 'database/index.html', context)

def table(request, table_name):
	klass = globals()[str(table_name)]
	table_rows = klass.objects.all()
	fields = [field.name for field in klass()._meta.fields]
	table = []
	for row in table_rows:
		colvals = []
		for field in fields:
			attr = getattr(row, field)
			try:
				colvals.append(attr.pk)
			except AttributeError:
				colvals.append(attr)
		table.append(colvals)

	context = {'table_name':table_name, 'table':table, 'fields':fields}
	return render(request, 'database/table.html', context)
	# return HttpResponse(template.render(context, request))