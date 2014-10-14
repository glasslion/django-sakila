# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Actor'
        db.create_table(u'actor', (
            ('actor_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'films', ['Actor'])

        # Adding model 'Category'
        db.create_table(u'category', (
            ('category_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'films', ['Category'])

        # Adding model 'Film'
        db.create_table(u'film', (
            ('film_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('release_year', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('language', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['films.Language'])),
            ('original_language', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name=u'filmAsOriginalLanguage', null=True, to=orm['films.Language'])),
            ('rental_duration', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('rental_rate', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2)),
            ('length', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
            ('replacement_cost', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('rating', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('special_features', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('fulltext', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'films', ['Film'])

        # Adding model 'FilmActor'
        db.create_table(u'film_actor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('actor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['films.Actor'])),
            ('film', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['films.Film'])),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'films', ['FilmActor'])

        # Adding model 'FilmCategory'
        db.create_table(u'film_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('film', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['films.Film'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['films.Category'])),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'films', ['FilmCategory'])

        # Adding model 'Language'
        db.create_table(u'language', (
            ('language_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'films', ['Language'])


    def backwards(self, orm):
        # Deleting model 'Actor'
        db.delete_table(u'actor')

        # Deleting model 'Category'
        db.delete_table(u'category')

        # Deleting model 'Film'
        db.delete_table(u'film')

        # Deleting model 'FilmActor'
        db.delete_table(u'film_actor')

        # Deleting model 'FilmCategory'
        db.delete_table(u'film_category')

        # Deleting model 'Language'
        db.delete_table(u'language')


    models = {
        u'films.actor': {
            'Meta': {'object_name': 'Actor', 'db_table': "u'actor'"},
            'actor_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'films': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['films.Film']", 'through': u"orm['films.FilmActor']", 'symmetrical': 'False'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'films.category': {
            'Meta': {'object_name': 'Category', 'db_table': "u'category'"},
            'category_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'films': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['films.Film']", 'through': u"orm['films.FilmCategory']", 'symmetrical': 'False'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        u'films.film': {
            'Meta': {'object_name': 'Film', 'db_table': "u'film'"},
            'actors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['films.Actor']", 'through': u"orm['films.FilmActor']", 'symmetrical': 'False'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['films.Category']", 'through': u"orm['films.FilmCategory']", 'symmetrical': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'film_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'fulltext': ('django.db.models.fields.TextField', [], {}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['films.Language']"}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'length': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'original_language': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "u'filmAsOriginalLanguage'", 'null': 'True', 'to': u"orm['films.Language']"}),
            'rating': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'release_year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rental_duration': ('django.db.models.fields.SmallIntegerField', [], {}),
            'rental_rate': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            'replacement_cost': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'special_features': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'films.filmactor': {
            'Meta': {'object_name': 'FilmActor', 'db_table': "u'film_actor'"},
            'actor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['films.Actor']"}),
            'film': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['films.Film']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'films.filmcategory': {
            'Meta': {'object_name': 'FilmCategory', 'db_table': "u'film_category'"},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['films.Category']"}),
            'film': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['films.Film']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'films.language': {
            'Meta': {'object_name': 'Language', 'db_table': "u'language'"},
            'language_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        }
    }

    complete_apps = ['films']