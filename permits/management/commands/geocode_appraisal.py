from django.core.management.base import BaseCommand, CommandError
from permits.models import AppraisalData
from googlegeocoder import GoogleGeocoder
import time

class Command(BaseCommand):
    def handle(self, *args, **options):
        appraisals_to_geocode = AppraisalData.objects.filter(latitude = None)


        for appraisal in appraisals_to_geocode:
            print appraisal
