import os
from django.contrib.gis.utils import LayerMapping

from models import CouncilDistrictsPrior

CouncilDistrictsPrior_mapping = {
    'district' : 'DISTRICT',
    'name' : 'NAME',
    'acres' : 'ACRES',
    'web' : 'WEB',
    'sq_miles' : 'Sq_Miles',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'mpoly'     : 'MULTIPOLYGON',
}

shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 
    'data/shp_files/city_of_sa_council_districts_prior_11_27_12/sPreviousCouncilDistrictsWGS84/sPreviousCouncilDistrictsWGS84.shp'))

def run(verbose=True):
    lm = LayerMapping(CouncilDistrictsPrior,shp,CouncilDistrictsPrior_mapping,transform=False, encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose)