from django.contrib.gis.db import models

class Permit(models.Model):
    permit_nr = models.CharField(max_length=12, unique=True)
    permit_date = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    permit_type = models.CharField(max_length=255, null=True)
    worktype = models.CharField(max_length=7, null=True)
    address = models.TextField(null=True)
    declvltn = models.DecimalField(max_digits=14, decimal_places=2, null=True)
    calcvltn = models.DecimalField(max_digits=14, decimal_places=2, null=True)
    temp_coodttm = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)
    coodttm = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)  
    latitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    geocode_accuracy = models.CharField(max_length=255, null=True)
    perm_point = models.PointField(null=True)


class Applicant(models.Model):
    apno = models.CharField(max_length=12)
    permit_nr = models.ForeignKey(Permit, to_field='permit_nr', null=True)
    aplty = models.CharField(max_length=3, null=True, blank=True)
    prim = models.CharField(max_length=3, null=True, blank=True)
    capacity = models.CharField(max_length=15, null=True, blank=True)
    capother = models.CharField(max_length=15, null=True, blank=True)
    nm = models.CharField(max_length=255, null=True, blank=True)
    dbaname = models.CharField(max_length=255, null=True, blank=True)

class Zoning(models.Model):
    apno = models.CharField(max_length=12)
    zoning = models.CharField(max_length=8, null=True, blank=True)
    descript = models.CharField(max_length=255, null=True, blank=True)
    permit_nr = models.ForeignKey(Permit, to_field='permit_nr', null=True)

class BexarTractsPop10(models.Model):
    #regular Django fields corresponding the attributes in the shapefile
    statefp10 = models.CharField(max_length=2, null=True, blank=True)
    countyfp10 = models.CharField(max_length=3, null=True, blank=True)
    tractce10 = models.CharField(max_length=6, null=True, blank=True)
    geoid10 = models.CharField(max_length=11, null=True, blank=True)
    name10 = models.CharField(max_length=7, null=True, blank=True)
    namelsad10 = models.CharField(max_length=20, null=True, blank=True)
    mtfcc10 = models.CharField(max_length=5, null=True, blank=True)
    funcstat10 = models.CharField(max_length=1, null=True, blank=True)
    aland10 = models.FloatField(null=True, blank=True)
    awater10 = models.FloatField(null=True, blank=True)
    intptlat10 = models.CharField(max_length=11, null=True, blank=True)
    intptlon10 = models.CharField(max_length=12, null=True, blank=True)
    sumlev = models.CharField(max_length=254, null=True, blank=True)
    state = models.CharField(max_length=254, null=True, blank=True)
    county = models.CharField(max_length=254, null=True, blank=True)
    cbsa = models.CharField(max_length=254, null=True, blank=True)
    csa = models.CharField(max_length=254, null=True, blank=True)
    necta = models.CharField(max_length=254, null=True, blank=True)
    cnecta = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    pop100 = models.CharField(max_length=254, null=True, blank=True)
    hu100 = models.CharField(max_length=254, null=True, blank=True)
    pop100_20 = models.CharField(max_length=254, null=True, blank=True)
    hu100_200 = models.CharField(max_length=254, null=True, blank=True)
    p001001 = models.CharField(max_length=254, null=True, blank=True)
    p001001_2 = models.CharField(max_length=254, null=True, blank=True)

    #geoDjango specific: geometry field (MultiPolygonField)
    #overriding the default manager with GeoManager instance

    mpoly = models.MultiPolygonField()
    objects = models.GeoManager()

class CouncilDistrictsPrior(models.Model):
    district = models.FloatField(null=True, blank=True)
    name = models.CharField(max_length=35, null=True, blank=True)
    acres = models.FloatField(null=True, blank=True)
    web = models.CharField(max_length=50, null=True, blank=True)
    sq_miles = models.IntegerField(null=True, blank=True)
    shape_leng = models.FloatField(null=True, blank=True)
    shape_area = models.FloatField(null=True, blank=True)

    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()

# This is an auto-generated Django model module created by ogrinspect.

class CouncilDistrictsPost(models.Model):
    district = models.FloatField()
    name = models.CharField(max_length=35)
    sqmiles = models.IntegerField()
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = models.MultiPolygonField(srid=4326)
    objects = models.GeoManager()

class ShapePermit(models.Model):
    permit_nr = models.CharField(max_length=254)
    permit_dat = models.CharField(max_length=254)
    permit_typ = models.CharField(max_length=254)
    worktype = models.CharField(max_length=254)
    address = models.CharField(max_length=254)
    declvltn = models.FloatField()
    calcvltn = models.FloatField()
    temp_coodt = models.CharField(max_length=254)
    coodttm = models.CharField(max_length=254)
    latitude = models.FloatField()
    longitude = models.FloatField()
    geocode_ac = models.CharField(max_length=254)
    geom = models.MultiPointField(srid=4326)
    objects = models.GeoManager()

class AppraisalData(models.Model):
    prop_id = models.CharField(max_length=255, blank=True)
    prop_yr = models.CharField(max_length=255, blank=True)
    geo_id = models.CharField(max_length=255, blank=True)
    owner_id = models.CharField(max_length=255, blank=True)
    owner_name = models.CharField(max_length=255, blank=True)
    addr_line1 = models.CharField(max_length=255, blank=True)
    addr_line2 = models.CharField(max_length=255, blank=True)
    addr_line3 = models.CharField(max_length=255, blank=True)
    addr_city = models.CharField(max_length=255, blank=True)
    addr_state = models.CharField(max_length=255, blank=True)
    country_cd = models.CharField(max_length=255, blank=True)
    zip = models.CharField(max_length=255, blank=True)
    zip4 = models.CharField(max_length=255, blank=True)
    yr_blt = models.CharField(max_length=255, blank=True)
    sq_ft = models.CharField(max_length=255, blank=True)
    land_acres = models.CharField(max_length=255, blank=True)
    imprv_hstd_val = models.CharField(max_length=255, blank=True)
    land_hstd_val = models.CharField(max_length=255, blank=True)
    state_cd = models.CharField(max_length=255, blank=True)
    market_val = models.CharField(max_length=255, blank=True)
    school = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    exemptions = models.CharField(max_length=255, blank=True)
    situs_num = models.CharField(max_length=255, blank=True)
    situs_street_prefix = models.CharField(max_length=255, blank=True)
    situs_street = models.CharField(max_length=255, blank=True)
    situs_street_sufix = models.CharField(max_length=255, blank=True)
    situs_unit = models.CharField(max_length=255, blank=True)
    dba_name = models.CharField(max_length=255, blank=True)
    imprv_type = models.CharField(max_length=255, blank=True)
    ext_wall = models.CharField(max_length=255, blank=True)
    roof = models.CharField(max_length=255, blank=True)
    foundation = models.CharField(max_length=255, blank=True)
    bedrooms = models.CharField(max_length=255, blank=True)
    whole_bath = models.CharField(max_length=255, blank=True)
    half_bath = models.CharField(max_length=255, blank=True)
    imprv_non_hstd_val = models.CharField(max_length=255, blank=True)
    land_non_hstd_val = models.CharField(max_length=255, blank=True)
    ag_use_val = models.CharField(max_length=255, blank=True)
    ag_market = models.CharField(max_length=255, blank=True)
    property_use_cd = models.CharField(max_length=255, blank=True)
    neighboorhoodcode = models.CharField(max_length=255, blank=True)
    legaldesc = models.CharField(max_length=255, blank=True)
    situs_zip = models.CharField(max_length=255, blank=True)
    num_unitn = models.CharField(max_length=255, blank=True)
    last_deed_date = models.CharField(max_length=255,blank=True)
    agent_id = models.CharField(max_length=255, blank=True)
    agent_name = models.CharField(max_length=255, blank=True)
    agent_addr_l1 = models.CharField(max_length=255, blank=True)
    agent_addr_l2 = models.CharField(max_length=255, blank=True)
    agent_addr_l3 = models.CharField(max_length=255, blank=True)
    agent_addr_city = models.CharField(max_length=255, blank=True)
    agent_addr_state = models.CharField(max_length=255, blank=True)
    agent_co_code = models.CharField(max_length=255, blank=True)
    agent_zip = models.CharField(max_length=255, blank=True)
    agent_zip4 = models.CharField(max_length=255, blank=True)
    prior_imp_hs_val = models.CharField(max_length=255, blank=True)
    prior_imp_non_hs_val = models.CharField(max_length=255, blank=True)
    priorld_hsval = models.CharField(max_length=255, blank=True)
    priorldnon_hs_val = models.CharField(max_length=255, blank=True)
    priorag_mkt = models.CharField(max_length=255, blank=True)
    priormktval = models.CharField(max_length=255, blank=True)
    bpplate_rend_penalty = models.CharField(max_length=255, blank=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, null=True, blank=True)
    geocode_accuracy = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)








