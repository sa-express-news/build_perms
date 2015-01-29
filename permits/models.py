from django.contrib.gis.db import models

class Permit(models.Model):
    permit_nr = models.CharField(max_length=12, unique=True)
    permit_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    permit_type = models.CharField(max_length=255, null=True)
    worktype = models.CharField(max_length=7, null=True)
    address = models.TextField(null=True)
    declvltn = models.DecimalField(max_digits=14, decimal_places=2, null=True)
    calcvltn = models.DecimalField(max_digits=14, decimal_places=2, null=True)
    temp_coodttm = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    coodttm = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)  
    latitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    geocode_accuracy = models.CharField(max_length=255, null=True)
    perm_point = models.PointField(null=True)

class Applicant(models.Model):
    apno = models.CharField(max_length=12)
    permit_nr = models.ForeignKey(Permit, to_field='permit_nr', null=True)
    aplty = models.CharField(max_length=3, null=True, blank=True)
    prim = models.CharField(max_length=3, null=True, blank=True)
    capacity = models.CharField(max_length=15, null=True, blank=True)
    capother = models.CharField(max_length=15, null=True, blank=True)
    nm = models.CharField(max_length=255, null=True, blank=True)
    dbaname = models.CharField(max_length=255, null=True, blank=True)

class Zoning(models.Model):
    apno = models.CharField(max_length=12)
    zoning = models.CharField(max_length=8, null=True, blank=True)
    descript = models.CharField(max_length=255, null=True, blank=True)
    permit_nr = models.ForeignKey(Permit, to_field='permit_nr', null=True)

class BexarTractsPop10(models.Model):
    #regular Django fields corresponding the attributes in the shapefile
    statefp10 = models.CharField(max_length=2, null=True, blank=True)
    countyfp10 = models.CharField(max_length=3, null=True, blank=True)
    tractce10 = models.CharField(max_length=6, null=True, blank=True)
    geoid10 = models.CharField(max_length=11, null=True, blank=True)
    name10 = models.CharField(max_length=7, null=True, blank=True)
    namelsad10 = models.CharField(max_length=20, null=True, blank=True)
    mtfcc10 = models.CharField(max_length=5, null=True, blank=True)
    funcstat10 = models.CharField(max_length=1, null=True, blank=True)
    aland10 = models.FloatField(null=True, blank=True)
    awater10 = models.FloatField(null=True, blank=True)
    intptlat10 = models.CharField(max_length=11, null=True, blank=True)
    intptlon10 = models.CharField(max_length=12, null=True, blank=True)
    sumlev = models.CharField(max_length=254, null=True, blank=True)
    state = models.CharField(max_length=254, null=True, blank=True)
    county = models.CharField(max_length=254, null=True, blank=True)
    cbsa = models.CharField(max_length=254, null=True, blank=True)
    csa = models.CharField(max_length=254, null=True, blank=True)
    necta = models.CharField(max_length=254, null=True, blank=True)
    cnecta = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    pop100 = models.CharField(max_length=254, null=True, blank=True)
    hu100 = models.CharField(max_length=254, null=True, blank=True)
    pop100_20 = models.CharField(max_length=254, null=True, blank=True)
    hu100_200 = models.CharField(max_length=254, null=True, blank=True)
    p001001 = models.CharField(max_length=254, null=True, blank=True)
    p001001_2 = models.CharField(max_length=254, null=True, blank=True)

    #geoDjango specific: geometry field (MultiPolygonField)
    #overriding the default manager with GeoManager instance

    mpoly = models.MultiPolygonField()
    objects = models.GeoManager()

class CouncilDistrictsPrior(models.Model):
    district = models.FloatField(null=True, blank=True)
    name = models.CharField(max_length=35, null=True, blank=True)
    acres = models.FloatField(null=True, blank=True)
    web = models.CharField(max_length=50, null=True, blank=True)
    sq_miles = models.IntegerField(null=True, blank=True)
    shape_leng = models.FloatField(null=True, blank=True)
    shape_area = models.FloatField(null=True, blank=True)

    mpoly = models.MultiPolygonField()
    objects = models.GeoManager()

# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models

class CouncilDistrictsPost(models.Model):
    district = models.FloatField()
    name = models.CharField(max_length=35)
    sqmiles = models.IntegerField()
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()