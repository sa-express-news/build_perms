# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'AppraisalData'
        db.delete_table(u'permits_appraisaldata')


    def backwards(self, orm):
        # Adding model 'AppraisalData'
        db.create_table(u'permits_appraisaldata', (
            ('agent_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('priorldnon_hs_val', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('dba_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('ag_market', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('agent_addr_city', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('prior_imp_non_hs_val', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('situs_street_sufix', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('market_val', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('yr_blt', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('roof', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('bpplate_rend_penalty', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('agent_co_code', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('agent_zip4', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('situs_street_prefix', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('ag_use_val', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('legaldesc', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('geocode_accuracy', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('ext_wall', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('sq_ft', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('imprv_type', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('agent_addr_l3', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('agent_addr_l2', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('agent_addr_l1', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=7, blank=True)),
            ('half_bath', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('country_cd', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('zip4', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('owner_id', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('foundation', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('agent_zip', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('owner_name', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('land_hstd_val', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('situs_street', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('property_use_cd', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('bedrooms', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('land_non_hstd_val', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('whole_bath', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('land_acres', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('imprv_non_hstd_val', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('neighboorhoodcode', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('agent_id', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('situs_num', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('prop_yr', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('prop_id', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('priorag_mkt', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('situs_zip', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('addr_city', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('school', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('situs_unit', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('num_unitn', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('prior_imp_hs_val', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('imprv_hstd_val', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('agent_addr_state', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=7, blank=True)),
            ('geo_id', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('priormktval', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('exemptions', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('state_cd', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('priorld_hsval', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('addr_state', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('addr_line1', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('addr_line2', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('addr_line3', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'permits', ['AppraisalData'])


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