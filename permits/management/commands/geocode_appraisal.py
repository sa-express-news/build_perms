from django.core.management.base import BaseCommand, CommandError
from permits.models import AppraisalData
from googlegeocoder import GoogleGeocoder
from permits.lib.batcher import batch_qs
import time
import re

class Command(BaseCommand):

    def handle(self, *args, **options):
        geocoder = GoogleGeocoder()
        appraisals_to_geocode = AppraisalData.objects.filter(latitude = None).order_by('id')

        for start, end, total, qs in batch_qs(appraisals_to_geocode):
            print "Now processing %s - %s of %s" % (start +1, end, total)
            
            for appraisal in qs:
                if appraisal.latitude == None and appraisal.longitude == None:

                    st_num = appraisal.situs_num.strip()
                    st_pref = appraisal.situs_street_prefix.strip()
                    street = appraisal.situs_street.strip()
                    str_suf = appraisal.situs_street_sufix.strip()
                    st_zip = ''

                    if appraisal.situs_zip != 'N/A':
                        st_zip = appraisal.situs_zip.strip()

                    city = appraisal.city
                    state = appraisal.situs_state
                    just_city = ''
                    
                    if re.search('(?<=CITY OF).*', city) is not None:
                        just_city = re.search('(?<=CITY OF).*', city).group(0).strip()

                    addy = "%s %s %s %s, %s, %s %s" % (st_num, st_pref, street, str_suf, just_city, state, st_zip)
                    print(addy)

                    try:
                        search = geocoder.get(addy)
                        time.sleep(1.5)
                        appraisal.latitude = search[0].geometry.location.lat
                        appraisal.longitude = search[0].geometry.location.lng 
                        appraisal.geocode_accuracy = search[0].geometry.location_type
                        print("Latitude: %s, Longitude: %s, Location type: %s") % (appraisal.latitude, appraisal.longitude, appraisal.geocode_accuracy)
                        appraisal.save()
                    except: 
                        print(("Couldn't geocode or already geocoded."))

