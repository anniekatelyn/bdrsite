# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Agar, Site, Run, Swabber, Plate, Isolate, Agar1Log, Agar2Log, Agar3Log, Agar4Log, Agar5Log, Agar6Log

admin.site.register(Agar)
admin.site.register(Site)
admin.site.register(Run)
admin.site.register(Swabber)
admin.site.register(Plate)
admin.site.register(Isolate)
admin.site.register(Agar1Log)
admin.site.register(Agar2Log)
admin.site.register(Agar3Log)
admin.site.register(Agar4Log)
admin.site.register(Agar5Log)
admin.site.register(Agar6Log)