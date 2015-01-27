import os
from django.contrib.gis.utils import LayerMapping
from models import BexarTractsPop10

BexarTractsPop10_mapping = {
    'statefp10' : 'STATEFP10',
    'countyfp10' : 'COUNTYFP10',
    'tractce10' : 'TRACTCE10',
    'geoid10' : 'GEOID10',
    'name10' : 'NAME10',
    'namelsad10' : 'NAMELSAD10',
    'mtfcc10' : 'MTFCC10',
    'funcstat10' : 'FUNCSTAT10',
    'aland10' : 'ALAND10',
    'awater10' : 'AWATER10',
    'intptlat10' : 'INTPTLAT10',
    'intptlon10' : 'INTPTLON10',
    'sumlev' : 'SUMLEV',
    'state' : 'STATE',
    'county' : 'COUNTY',
    'cbsa' : 'CBSA',
    'csa' : 'CSA',
    'necta' : 'NECTA',
    'cnecta' : 'CNECTA',
    'name' : 'NAME',
    'pop100' : 'POP100',
    'hu100' : 'HU100',
    'pop100_20' : 'POP100.20',
    'hu100_200' : 'HU100.200',
    'p001001' : 'P001001',
    'p001001_2' : 'P001001.2',
    'mpoly' : 'MULTIPOLYGON',
    
}

shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/shp_files/bexar_tracts_10_census/bexar_tracts_with_census_data_10.shp'))

def run(verbose=True):
    lm = LayerMapping(BexarTractsPop10, shp, BexarTractsPop10_mapping, transform=False, encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose)
