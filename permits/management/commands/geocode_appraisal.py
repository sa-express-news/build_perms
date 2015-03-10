from django.core.management.base import BaseCommand, CommandError
from permits.models import AppraisalData
from googlegeocoder import GoogleGeocoder
from permits.lib.batcher import batch_qs
import time

class Command(BaseCommand):

    def handle(self, *args, **options):
        geocoder = GoogleGeocoder()
        batch_qs("helos")
        appraisals_to_geocode = AppraisalData.objects.filter(latitude = None).order_by('id')

        for start, end, total, qs in batch_qs(appraisals_to_geocode):
            print "Now processing %s - %s of %s" % (start +1, end, total)
            
            for appraisal in qs:
                st_num = appraisal.situs_num
                st_pref = appraisal.situs_street_prefix
                street = appraisal.situs_street
                str_suf = appraisal.situs_street_sufix
                zip = appraisal.situs_zip
                addy = "%s %s %s %s" % (st_num, st_pref, street, str_suf)
                print(addy)         
