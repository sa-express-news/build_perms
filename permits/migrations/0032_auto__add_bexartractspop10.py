# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BexarTractsPop10'
        db.create_table(u'permits_bexartractspop10', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('statefp10', self.gf('django.db.models.fields.CharField')(max_length=2, null=True, blank=True)),
            ('countyfp10', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('tractce10', self.gf('django.db.models.fields.CharField')(max_length=6, null=True, blank=True)),
            ('geoid10', self.gf('django.db.models.fields.CharField')(max_length=11, null=True, blank=True)),
            ('name10', self.gf('django.db.models.fields.CharField')(max_length=7, null=True, blank=True)),
            ('namelsad10', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('mtfcc10', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True)),
            ('funcstat10', self.gf('django.db.models.fields.CharField')(max_length=1, null=True, blank=True)),
            ('aland10', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('awater10', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('intptlat10', self.gf('django.db.models.fields.CharField')(max_length=11, null=True, blank=True)),
            ('intptlon10', self.gf('django.db.models.fields.CharField')(max_length=12, null=True, blank=True)),
            ('sumlev', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('county', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('cbsa', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('csa', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('necta', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('cnecta', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('pop100', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('hu100', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('pop100_20', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('hu100_200', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('p001001', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('p001001_2', self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True)),
            ('mpoly', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')()),
        ))
        db.send_create_signal(u'permits', ['BexarTractsPop10'])


    def backwards(self, orm):
        # Deleting model 'BexarTractsPop10'
        db.delete_table(u'permits_bexartractspop10')


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