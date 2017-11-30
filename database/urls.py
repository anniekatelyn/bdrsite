from django.conf.urls import url

from . import views, models
import inspect
import re

urlpatterns = [
    url(r'^$', views.index, name='index'),
]

# add table names from model
table_names = []
for name, obj in inspect.getmembers(models):
	if inspect.isclass(obj):
		table_names.append(obj.__name__)

for table_name in table_names:
	regex = '^(?P<table_name>' + re.escape(table_name) + ')/$'
	# urlpatterns.append(url(r'^(?P<table_id>\\table_name)' + r'/$', views.table, name='table'))
	urlpatterns.append(url(regex, views.table, name='table'))