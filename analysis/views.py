# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import inspect
from .forms import QueryForm, QueryDropdownForm
from .models import QueryDropdown
from django.db import connection
from highcharts.views import HighChartsBarView


query_dict = {'1':'SELECT site_id, cfu, ctx FROM plate JOIN agar ON plate.agar_id = agar.agar_id', '2':'two'}

def index(request): # GET
	# create blank forms
	template_name = 'analysis/index.html'
	sql_form = QueryForm()
	dropdown_form = QueryDropdownForm()
	return render(request, template_name, {'sql_form': sql_form, 'dropdown_form': dropdown_form})

def get_query(request): # POST
	# create a form instance and populate it with data from the request
	sql_form = QueryForm(request.POST)
	# check if it's valid
	if sql_form.is_valid(): 
		# process the data in form.cleaned_data as required
		query = sql_form.cleaned_data['query']
		result = execute_query(query)
		colnames = result[0].keys
		num_rows = len(result)
		return render(request, 'analysis/query.html', {'query':query, 'num_rows':num_rows, 'result':result, 'colnames':colnames})
	else:
		return HttpResponse("Could not execute query.")

def get_selection(request):
	dropdown_form = QueryDropdownForm(request.POST)
	if dropdown_form.is_valid():
		query_num = dropdown_form.cleaned_data['query']
		query = query_dict[query_num]
		result = execute_query(query)
		colnames = result[0].keys
		num_rows = len(result)
		# return BarView.as_view()
		return render(request, 'analysis/query.html', {'query':query, 'num_rows':num_rows, 'result':result, 'colnames':colnames, 'preselected':True})
	else:
		return HttpResponse("Could not execute selection.")

def execute_query(query):
	with connection.cursor() as cursor:
		cursor.execute(query)
		return dictfetchall(cursor)
	# ex: [{'parent_id': None, 'id': 54360982}, {'parent_id': None, 'id': 54360880}]

def dictfetchall(cursor):
	# Return all rows from a cursor as a dict
	columns = [col[0] for col in cursor.description]
	return [
    	dict(zip(columns, row))
    	for row in cursor.fetchall()
    ]

class BarView(HighChartsBarView):
	title = 'Example Bar Chart'
	subtitle = 'my subtitle'
	categories = ['Orange', 'Bananas', 'Apples']
	@property
	def series(self):
		series = [
			{
				'name': 'Orange',
				'type': 'column',
				'yAxis': 1,
				'data': [90,44,55,67,4,5,6,3,2,45,2,3,2,45,5],
				'tooltip': "{ valueSuffix: ' euro' }",
				'color': '#3771c8'
			},
			{
				'name': 'Bananas',
				'type': 'spline',
				'yAxis': 2,
				'data': [12,34,34,34, 5,34,3,45,2,3,2,4,4,1,23],
				'marker': { 'enabled': 'true' },
				'dashStyle': 'shortdot',
				'color': '#666666',
			},
			{
				'name': 'Apples',
				'type': 'spline',
				'data': [12,23,23,23,21,4,4,76,3,66,6,4,5,2,3],
				'color': '#f67d0a'
			}
		]
		return series


