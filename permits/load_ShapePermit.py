import os
from django.contrib.gis.utils import LayerMapping
from models import ShapePermit

shapepermit_mapping = {
    'permit_nr' : 'permit_nr',
    'permit_dat' : 'permit_dat',
    'permit_typ' : 'permit_typ',
    'worktype' : 'worktype',
    'address' : 'address',
    'declvltn' : 'declvltn',
    'calcvltn' : 'calcvltn',
    'temp_coodt' : 'temp_coodt',
    'coodttm' : 'coodttm',
    'latitude' : 'latitude',
    'longitude' : 'longitude',
    'geocode_ac' : 'geocode_ac',
    'geom' : 'MULTIPOINT',
}

shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/shp_files/permits_shp/permits_wgs84.shp'))

def run(verbose=True):
    lm = LayerMapping(ShapePermit, shp, shapepermit_mapping, source_srs=4326, transform=False, encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose)

    