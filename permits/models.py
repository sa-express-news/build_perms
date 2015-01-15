from django.db import models

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
    