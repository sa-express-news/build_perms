from django.core.management.base import BaseCommand, CommandError
from permits.models import Applicant, Permit, Zoning
import os
import csv

class Command(BaseCommand):
    def handle(self, *args, **options):
        counter = 1
        filepath = os.path.join( os.path.dirname ( __file__ ), '..', '..', 'data' )
        zoning_csv = open(os.path.join(filepath, 'permits_03_07_excel', 'zoning_03_07.csv'))
        zonings = csv.DictReader(zoning_csv)

        for zoning in zonings:
            try:
                permit_nr = zoning['apno']
                permit = Permit.objects.get(permit_nr = permit_nr)
                Zoning.objects.create(permit_nr=permit, **zoning)
                print("saving record %s") % counter
                counter += 1
            except Permit.DoesNotExist:
                print("Permit.DoesNotExist")
