from django.core.management.base import BaseCommand, CommandError
from permits.models import Permit
from googlegeocoder import GoogleGeocoder
import time

class Command(BaseCommand):

    def handle(self, *args, **options):
        geocoder = GoogleGeocoder()
        permits = Permit.objects.all()

        for permit in permits:
            if permit.latitude == None and permit.longitude == None:
                try:
                    search = geocoder.get(permit.address)
                    time.sleep(1.5)
                    permit.latitude = search[0].geometry.location.lat
                    permit.longitude = search[0].geometry.location.lng
                    permit.geocode_accuracy = search[0].geometry.location_type
                    print("Latitude: %s, Longitude: %s, Location type: %s") % ( permit.latitude, permit.longitude, permit.geocode_accuracy )
                    permit.save()
                except:
                    print("Couldn't geocode...")
