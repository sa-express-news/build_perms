# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Renaming column for 'Applicant.apno' to match new field type.
        db.rename_column(u'permits_applicant', 'apno_id', 'apno')
        # Changing field 'Applicant.apno'
        db.alter_column(u'permits_applicant', 'apno', self.gf('django.db.models.fields.CharField')(unique=True, max_length=12))
        # Removing index on 'Applicant', fields ['apno']
        db.delete_index(u'permits_applicant', ['apno_id'])

        # Adding unique constraint on 'Applicant', fields ['apno']
        db.create_unique(u'permits_applicant', ['apno'])


    def backwards(self, orm):
        # Removing unique constraint on 'Applicant', fields ['apno']
        db.delete_unique(u'permits_applicant', ['apno'])

        # Adding index on 'Applicant', fields ['apno']
        db.create_index(u'permits_applicant', ['apno_id'])


        # Renaming column for 'Applicant.apno' to match new field type.
        db.rename_column(u'permits_applicant', 'apno', 'apno_id')
        # Changing field 'Applicant.apno'
        db.alter_column(u'permits_applicant', 'apno_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['permits.Permit'], to_field='permit_nr'))

    models = {
        u'permits.applicant': {
            'Meta': {'object_name': 'Applicant'},
            'aplty': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'apno': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '12'}),
            'capacity': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'capother': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'dbaname': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nm': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'prim': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'})
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
            'permit_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'permit_nr': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '12'}),
            'permit_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'temp_coodttm': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'worktype': ('django.db.models.fields.CharField', [], {'max_length': '7', 'null': 'True'})
        }
    }

    complete_apps = ['permits']