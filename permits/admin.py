from django.contrib.gis import admin 
from models import BexarTractsPop10

admin.site.register(BexarTractsPop10, admin.GeoModelAdmin)