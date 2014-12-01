from django.db import models

class Permit(models.Model):
    permit_nr = models.CharField(max_length=12, unique=True)
    
