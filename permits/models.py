from django.db import models

class Permit(models.Model):
    permit_nr = models.CharField(max_length=12, unique=True)
    permit_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    permit_type = models.CharField(max_length=255, null=True)
    worktype = models.CharField(max_length=7, null=True)
    address = models.TextField(null=True)
