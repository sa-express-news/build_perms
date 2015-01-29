import os
from django.contrib.gis.utils import LayerMapping
from models import CouncilDistrictsPost

# Auto-generated `LayerMapping` dictionary for CouncilDistrictsPost model
councildistrictspost_mapping = {
    'district' : 'District',
    'name' : 'Name',
    'sqmiles' : 'SqMiles',
    'shape_leng' : 'Shape_Leng',
    'shape_area' : 'Shape_Area',
    'geom' : 'MULTIPOLYGON',
}

shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/shp_files/city_of_sa_council_districts_post_11_27_12/sCoSACouncilDistrictsWGS84/sCoSACouncilDistrictsWGS84.shp'))

def run(verbose=True):
    lm = LayerMapping(CouncilDistrictsPost, shp, councildistrictspost_mapping, transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)
    