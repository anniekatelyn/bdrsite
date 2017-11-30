# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

QUERY_CHOICES = (
	('1','Relative Abundance/Resistance of Plated Samples'),
	('2','Other'),)

class QueryDropdown(models.Model):
	query = models.CharField(max_length=200,choices=QUERY_CHOICES)