from django.core.management.base import BaseCommand, CommandError
from permits.models import Permit
import os
import csv


class Command(BaseCommand):

    def handle(self, *args, **options):
        counter = 1
        filepath = os.path.join( os.path.dirname ( __file__), os.path.pardir, os.path.pardir, 'data')
        
        permits_csv = open(os.path.join(filepath, 'permits_03_07.csv'))
        permits = csv.DictReader(permits_csv)

        for permit in permits:
            record = Permit(**permit)

            if record.temp_coodttm == "":
                record.temp_coodttm = None

            if record.coodttm == "":
                record.coodttm = None

            # if record.latitude == "":
            #     record.latitude = None

            # if record.longitude == "":
            #     record.longitude = None

            print("saving new permit %s of 54,399") % counter
            record.save()
            counter += 1
                
