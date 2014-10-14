# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Address'
        db.create_table(u'address', (
            ('address_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('address2', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('district', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['addresses.City'])),
            ('postal_code', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'addresses', ['Address'])

        # Adding model 'City'
        db.create_table(u'city', (
            ('city_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('country', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['addresses.Country'])),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'addresses', ['City'])

        # Adding model 'Country'
        db.create_table(u'country', (
            ('country_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'addresses', ['Country'])


    def backwards(self, orm):
        # Deleting model 'Address'
        db.delete_table(u'address')

        # Deleting model 'City'
        db.delete_table(u'city')

        # Deleting model 'Country'
        db.delete_table(u'country')


    models = {
        u'addresses.address': {
            'Meta': {'object_name': 'Address', 'db_table': "u'address'"},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'address2': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'address_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['addresses.City']"}),
            'district': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'})
        },
        u'addresses.city': {
            'Meta': {'object_name': 'City', 'db_table': "u'city'"},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'city_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['addresses.Country']"}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'addresses.country': {
            'Meta': {'object_name': 'Country', 'db_table': "u'country'"},
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'country_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['addresses']