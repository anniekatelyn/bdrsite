# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Agar(models.Model):
	class Meta:
		db_table = 'agar'
	agar_id = models.IntegerField(primary_key=True)
	media = models.CharField(max_length=100)
	temp = models.CharField(max_length=20)
	ctx = models.BooleanField()
	def __str__(self):
		return str(self.agar_id) + " " + self.media + " " + self.temp + " " + str(int(self.ctx))

class Site(models.Model):
	class Meta:
		db_table = 'site'
	site_id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=200, unique=True)
	def __str__(self):
		return str(self.site_id) + " " + self.name

class Run(models.Model):
	class Meta:
		db_table = 'run'
	run_id = models.IntegerField(primary_key=True)
	date = models.DateField()
	time = models.TimeField()
	conditions = models.TextField(default="")
	initials = models.CharField(max_length=20)
	def __str__(self):
		return str(self.run_id) + " " + str(self.date) + " " + str(self.time) + " " + self.conditions + self.initials

class Swabber(models.Model):
	class Meta:
		db_table = 'swabber'
	# run_id = models.IntegerField(primary_key=True)
	run_id = models.ForeignKey(Run, db_column="run_id", on_delete=models.CASCADE, primary_key=True)
	swabber = models.CharField(max_length=20)
	def __str__(self):
		return str(self.run_id.run_id) + " " + self.swabber

class Plate(models.Model):
	class Meta:
		db_table = 'plate'
	plate_id = models.IntegerField(primary_key=True)
	run_id = models.ForeignKey('Run', db_column="run_id", on_delete=models.CASCADE)
	site_id = models.ForeignKey('Site', db_column="site_id", on_delete=models.CASCADE)
	agar_id = models.ForeignKey('Agar', db_column="agar_id", on_delete=models.CASCADE)
	cfu = models.IntegerField()
	def __str__(self):
		return str(self.plate_id) + " " + str(self.run_id.run_id) + " " + str(self.site_id.site_id) + " " + str(self.agar_id.agar_id) + " " + str(self.cfu)

class Isolate(models.Model):
	class Meta:
		db_table = 'isolate'
	iso_id = models.IntegerField(primary_key=True)
	plate_id = models.ForeignKey(Plate, db_column="plate_id", on_delete=models.CASCADE)
	def __str__(self):
		return str(self.iso_id) + " " + str(self.plate_id.plate_id)

class Agar1Log(models.Model):
	class Meta:
		db_table = 'agar1log'
	run_id = models.ForeignKey('Run', db_column="run_id", on_delete=models.CASCADE, primary_key=True)
	site_1 = models.IntegerField(null=True)
	site_2 = models.IntegerField(null=True)
	site_3 = models.IntegerField(null=True)
	site_4 = models.IntegerField(null=True)
	site_5 = models.IntegerField(null=True)
	site_6 = models.IntegerField(null=True)
	site_7 = models.IntegerField(null=True)
	site_8 = models.IntegerField(null=True)
	site_9 = models.IntegerField(null=True)
	site_10 = models.IntegerField(null=True)
	site_11 = models.IntegerField(null=True)
	site_12 = models.IntegerField(null=True)
	site_13 = models.IntegerField(null=True)
	site_14 = models.IntegerField(null=True)
	site_15 = models.IntegerField(null=True)
	site_16 = models.IntegerField(null=True)
	site_17 = models.IntegerField(null=True)
	def __str__(self):
		return str(self.run_id.run_id) + "\t" + str(self.site_1) + "\t" + str(self.site_2) + "\t" + str(self.site_3) + "\t" + str(self.site_4)
		+ "\t" + str(self.site_5) + "\t" + str(self.site_6) + "\t" + str(self.site_7) + "\t" + str(self.site_8) + "\t" + str(self.site_9)
		+ "\t" + str(self.site_10) + "\t" + str(self.site_11) + "\t" + str(self.site_12) + "\t" + str(self.site_13) + "\t" + str(self.site_14) 
		+ "\t" + str(self.site_15) + "\t" + str(self.site_16) + "\t" + str(self.site_17)

class Agar2Log(models.Model):
	class Meta:
		db_table = 'agar2log'
	run_id = models.ForeignKey('Run', db_column="run_id", on_delete=models.CASCADE, primary_key=True)
	site_1 = models.IntegerField(null=True)
	site_2 = models.IntegerField(null=True)
	site_3 = models.IntegerField(null=True)
	site_4 = models.IntegerField(null=True)
	site_5 = models.IntegerField(null=True)
	site_6 = models.IntegerField(null=True)
	site_7 = models.IntegerField(null=True)
	site_8 = models.IntegerField(null=True)
	site_9 = models.IntegerField(null=True)
	site_10 = models.IntegerField(null=True)
	site_11 = models.IntegerField(null=True)
	site_12 = models.IntegerField(null=True)
	site_13 = models.IntegerField(null=True)
	site_14 = models.IntegerField(null=True)
	site_15 = models.IntegerField(null=True)
	site_16 = models.IntegerField(null=True)
	site_17 = models.IntegerField(null=True)
	def __str__(self):
		return str(self.run_id.run_id) + "\t" + str(self.site_1) + "\t" + str(self.site_2) + "\t" + str(self.site_3) + "\t" + str(self.site_4)
		+ "\t" + str(self.site_5) + "\t" + str(self.site_6) + "\t" + str(self.site_7) + "\t" + str(self.site_8) + "\t" + str(self.site_9)
		+ "\t" + str(self.site_10) + "\t" + str(self.site_11) + "\t" + str(self.site_12) + "\t" + str(self.site_13) + "\t" + str(self.site_14) 

class Agar3Log(models.Model):
	class Meta:
		db_table = 'agar3log'
	run_id = models.ForeignKey('Run', db_column="run_id", on_delete=models.CASCADE, primary_key=True)
	site_1 = models.IntegerField(null=True)
	site_2 = models.IntegerField(null=True)
	site_3 = models.IntegerField(null=True)
	site_4 = models.IntegerField(null=True)
	site_5 = models.IntegerField(null=True)
	site_6 = models.IntegerField(null=True)
	site_7 = models.IntegerField(null=True)
	site_8 = models.IntegerField(null=True)
	site_9 = models.IntegerField(null=True)
	site_10 = models.IntegerField(null=True)
	site_11 = models.IntegerField(null=True)
	site_12 = models.IntegerField(null=True)
	site_13 = models.IntegerField(null=True)
	site_14 = models.IntegerField(null=True)
	site_15 = models.IntegerField(null=True)
	site_16 = models.IntegerField(null=True)
	site_17 = models.IntegerField(null=True)
	def __str__(self):
		return str(self.run_id.run_id) + "\t" + str(self.site_1) + "\t" + str(self.site_2) + "\t" + str(self.site_3) + "\t" + str(self.site_4)
		+ "\t" + str(self.site_5) + "\t" + str(self.site_6) + "\t" + str(self.site_7) + "\t" + str(self.site_8) + "\t" + str(self.site_9)
		+ "\t" + str(self.site_10) + "\t" + str(self.site_11) + "\t" + str(self.site_12) + "\t" + str(self.site_13) + "\t" + str(self.site_14) 

class Agar4Log(models.Model):
	class Meta:
		db_table = 'agar4log'
	run_id = models.ForeignKey('Run', db_column="run_id", on_delete=models.CASCADE, primary_key=True)
	site_1 = models.IntegerField(null=True)
	site_2 = models.IntegerField(null=True)
	site_3 = models.IntegerField(null=True)
	site_4 = models.IntegerField(null=True)
	site_5 = models.IntegerField(null=True)
	site_6 = models.IntegerField(null=True)
	site_7 = models.IntegerField(null=True)
	site_8 = models.IntegerField(null=True)
	site_9 = models.IntegerField(null=True)
	site_10 = models.IntegerField(null=True)
	site_11 = models.IntegerField(null=True)
	site_12 = models.IntegerField(null=True)
	site_13 = models.IntegerField(null=True)
	site_14 = models.IntegerField(null=True)
	site_15 = models.IntegerField(null=True)
	site_16 = models.IntegerField(null=True)
	site_17 = models.IntegerField(null=True)
	def __str__(self):
		return str(self.run_id.run_id) + "\t" + str(self.site_1) + "\t" + str(self.site_2) + "\t" + str(self.site_3) + "\t" + str(self.site_4)
		+ "\t" + str(self.site_5) + "\t" + str(self.site_6) + "\t" + str(self.site_7) + "\t" + str(self.site_8) + "\t" + str(self.site_9)
		+ "\t" + str(self.site_10) + "\t" + str(self.site_11) + "\t" + str(self.site_12) + "\t" + str(self.site_13) + "\t" + str(self.site_14) 

class Agar5Log(models.Model):
	class Meta:
		db_table = 'agar5log'
	run_id = models.ForeignKey('Run', db_column="run_id", on_delete=models.CASCADE, primary_key=True)
	site_1 = models.IntegerField(null=True)
	site_2 = models.IntegerField(null=True)
	site_3 = models.IntegerField(null=True)
	site_4 = models.IntegerField(null=True)
	site_5 = models.IntegerField(null=True)
	site_6 = models.IntegerField(null=True)
	site_7 = models.IntegerField(null=True)
	site_8 = models.IntegerField(null=True)
	site_9 = models.IntegerField(null=True)
	site_10 = models.IntegerField(null=True)
	site_11 = models.IntegerField(null=True)
	site_12 = models.IntegerField(null=True)
	site_13 = models.IntegerField(null=True)
	site_14 = models.IntegerField(null=True)
	site_15 = models.IntegerField(null=True)
	site_16 = models.IntegerField(null=True)
	site_17 = models.IntegerField(null=True)
	def __str__(self):
		return str(self.run_id.run_id) + "\t" + str(self.site_1) + "\t" + str(self.site_2) + "\t" + str(self.site_3) + "\t" + str(self.site_4)
		+ "\t" + str(self.site_5) + "\t" + str(self.site_6) + "\t" + str(self.site_7) + "\t" + str(self.site_8) + "\t" + str(self.site_9)
		+ "\t" + str(self.site_10) + "\t" + str(self.site_11) + "\t" + str(self.site_12) + "\t" + str(self.site_13) + "\t" + str(self.site_14) 

class Agar6Log(models.Model):
	class Meta:
		db_table = 'agar6log'
	run_id = models.ForeignKey('Run', db_column="run_id", on_delete=models.CASCADE, primary_key=True)
	site_1 = models.IntegerField(null=True)
	site_2 = models.IntegerField(null=True)
	site_3 = models.IntegerField(null=True)
	site_4 = models.IntegerField(null=True)
	site_5 = models.IntegerField(null=True)
	site_6 = models.IntegerField(null=True)
	site_7 = models.IntegerField(null=True)
	site_8 = models.IntegerField(null=True)
	site_9 = models.IntegerField(null=True)
	site_10 = models.IntegerField(null=True)
	site_11 = models.IntegerField(null=True)
	site_12 = models.IntegerField(null=True)
	site_13 = models.IntegerField(null=True)
	site_14 = models.IntegerField(null=True)
	site_15 = models.IntegerField(null=True)
	site_16 = models.IntegerField(null=True)
	site_17 = models.IntegerField(null=True)
	def __str__(self):
		return str(self.run_id.run_id) + "\t" + str(self.site_1) + "\t" + str(self.site_2) + "\t" + str(self.site_3) + "\t" + str(self.site_4)
		+ "\t" + str(self.site_5) + "\t" + str(self.site_6) + "\t" + str(self.site_7) + "\t" + str(self.site_8) + "\t" + str(self.site_9)
		+ "\t" + str(self.site_10) + "\t" + str(self.site_11) + "\t" + str(self.site_12) + "\t" + str(self.site_13) + "\t" + str(self.site_14) 


