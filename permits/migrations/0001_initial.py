# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Permit'
        db.create_table(u'permits_permit', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('permit_nr', self.gf('django.db.models.fields.CharField')(unique=True, max_length=12)),
        ))
        db.send_create_signal(u'permits', ['Permit'])


    def backwards(self, orm):
        # Deleting model 'Permit'
        db.delete_table(u'permits_permit')


    models = {
        u'permits.permit': {
            'Meta': {'object_name': 'Permit'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'permit_nr': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '12'})
        }
    }

    complete_apps = ['permits']