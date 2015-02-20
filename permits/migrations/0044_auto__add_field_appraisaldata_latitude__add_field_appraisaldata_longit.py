# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'AppraisalData.latitude'
        db.add_column(u'permits_appraisaldata', 'latitude',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=7, blank=True),
                      keep_default=False)

        # Adding field 'AppraisalData.longitude'
        db.add_column(u'permits_appraisaldata', 'longitude',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=7, blank=True),
                      keep_default=False)

        # Adding field 'AppraisalData.geocode_accuracy'
        db.add_column(u'permits_appraisaldata', 'geocode_accuracy',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'AppraisalData.latitude'
        db.delete_column(u'permits_appraisaldata', 'latitude')

        # Deleting field 'AppraisalData.longitude'
        db.delete_column(u'permits_appraisaldata', 'longitude')

        # Deleting field 'AppraisalData.geocode_accuracy'
        db.delete_column(u'permits_appraisaldata', 'geocode_accuracy')


    models = {
        u'permits.applicant': {
            'Meta': {'object_name': 'Applicant'},
            'aplty': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'apno': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'capacity': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'capother': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'dbaname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nm': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'permit_nr': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['permits.Permit']", 'to_field': "'permit_nr'", 'null': 'True'}),
            'prim': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'})
        },
        u'permits.appraisaldata': {
            'Meta': {'object_name': 'AppraisalData'},
            'addr_city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'addr_line1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'addr_line2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'addr_line3': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'addr_state': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'ag_market': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'ag_use_val': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'agent_addr_city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'agent_addr_l1': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'agent_addr_l2': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'agent_addr_l3': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'agent_addr_state': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'agent_co_code': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'agent_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'agent_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'agent_zip': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'agent_zip4': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'bedrooms': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'bpplate_rend_penalty': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'country_cd': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'dba_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'exemptions': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'ext_wall': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'foundation': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'geo_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'geocode_accuracy': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'half_bath': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imprv_hstd_val': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'imprv_non_hstd_val': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'imprv_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'land_acres': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'land_hstd_val': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'land_non_hstd_val': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '7', 'blank': 'True'}),
            'legaldesc': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '7', 'blank': 'True'}),
            'market_val': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'neighboorhoodcode': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'num_unitn': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'owner_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'owner_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'prior_imp_hs_val': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'prior_imp_non_hs_val': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'priorag_mkt': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'priorld_hsval': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'priorldnon_hs_val': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'priormktval': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'prop_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'prop_yr': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'property_use_cd': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'roof': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'school': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'situs_num': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'situs_street': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'situs_street_prefix': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'situs_street_sufix': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'situs_unit': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'situs_zip': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'sq_ft': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'state_cd': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'whole_bath': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'yr_blt': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'zip4': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        u'permits.bexartractspop10': {
            'Meta': {'object_name': 'BexarTractsPop10'},
            'aland10': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'awater10': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'cbsa': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'cnecta': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'county': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'countyfp10': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'csa': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'funcstat10': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'geoid10': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'hu100': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'hu100_200': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intptlat10': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'intptlon10': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'mpoly': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'mtfcc10': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'name10': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True', 'blank': 'True'}),
            'namelsad10': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'necta': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'p001001': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'p001001_2': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'pop100': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'pop100_20': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'statefp10': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'sumlev': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'tractce10': ('django.db.models.fields.CharField', [], {'max_length': '6', 'null': 'True', 'blank': 'True'})
        },
        u'permits.councildistrictspost': {
            'Meta': {'object_name': 'CouncilDistrictsPost'},
            'district': ('django.db.models.fields.FloatField', [], {}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'shape_area': ('django.db.models.fields.FloatField', [], {}),
            'shape_leng': ('django.db.models.fields.FloatField', [], {}),
            'sqmiles': ('django.db.models.fields.IntegerField', [], {})
        },
        u'permits.councildistrictsprior': {
            'Meta': {'object_name': 'CouncilDistrictsPrior'},
            'acres': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'district': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35', 'null': 'True', 'blank': 'True'}),
            'shape_area': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'shape_leng': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'sq_miles': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'web': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        u'permits.permit': {
            'Meta': {'object_name': 'Permit'},
            'address': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'calcvltn': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '14', 'decimal_places': '2'}),
            'coodttm': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'declvltn': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '14', 'decimal_places': '2'}),
            'geocode_accuracy': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '7', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '7', 'blank': 'True'}),
            'perm_point': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True'}),
            'permit_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'permit_nr': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '12'}),
            'permit_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'temp_coodttm': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'worktype': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True'})
        },
        u'permits.shapepermit': {
            'Meta': {'object_name': 'ShapePermit'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'calcvltn': ('django.db.models.fields.FloatField', [], {}),
            'coodttm': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'declvltn': ('django.db.models.fields.FloatField', [], {}),
            'geocode_ac': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'geom': ('django.contrib.gis.db.models.fields.MultiPointField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.FloatField', [], {}),
            'longitude': ('django.db.models.fields.FloatField', [], {}),
            'permit_dat': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'permit_nr': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'permit_typ': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'temp_coodt': ('django.db.models.fields.CharField', [], {'max_length': '254'}),
            'worktype': ('django.db.models.fields.CharField', [], {'max_length': '254'})
        },
        u'permits.zoning': {
            'Meta': {'object_name': 'Zoning'},
            'apno': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'descript': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'permit_nr': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['permits.Permit']", 'to_field': "'permit_nr'", 'null': 'True'}),
            'zoning': ('django.db.models.fields.CharField', [], {'max_length': '8', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['permits']