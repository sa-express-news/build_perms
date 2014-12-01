# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Permit.permit_type'
        db.add_column(u'permits_permit', 'permit_type',
                      self.gf('django.db.models.fields.CharField')(max_length=255, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Permit.permit_type'
        db.delete_column(u'permits_permit', 'permit_type')


    models = {
        u'permits.permit': {
            'Meta': {'object_name': 'Permit'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'permit_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'permit_nr': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '12'}),
            'permit_type': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'})
        }
    }

    complete_apps = ['permits']