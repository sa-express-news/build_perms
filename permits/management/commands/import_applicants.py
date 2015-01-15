from django.core.management.base import BaseCommand, CommandError
from permits.models import Applicant, Permit
import os
import csv

class Command(BaseCommand):
    def handle(self, *args, **options):
        counter = 1
        filepath = os.path.join( os.path.dirname ( __file__), '..', '..', 'data', )
        applicants_csv = open(os.path.join(filepath, 'applicants.csv'))
        applicants = csv.DictReader(applicants_csv)


        for applicant in applicants:
            try:
                permit_nr = applicant['apno']
                permit = Permit.objects.get(permit_nr = permit_nr)
                record = Applicant(**applicant)
                record.permit_nr = permit
                record.save() 
                print("saving record %s") % counter
                counter += 1
            except Permit.DoesNotExist:
                applicants.next()
            continue

