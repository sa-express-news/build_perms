# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Applicant'
        db.delete_table(u'permits_applicant')


    def backwards(self, orm):
        # Adding model 'Applicant'
        db.create_table(u'permits_applicant', (
            ('permit_nr', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['permits.Permit'], to_field='permit_nr', null=True)),
            ('capacity', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('nm', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('capother', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('prim', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('dbaname', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('aplty', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('apno', self.gf('django.db.models.fields.CharField')(max_length=12)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'permits', ['Applicant'])


    models = {
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
            'permit_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'permit_nr': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '12'}),
            'permit_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'temp_coodttm': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'worktype': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True'})
        }
    }

    complete_apps = ['permits']