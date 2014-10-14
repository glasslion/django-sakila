# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Customer'
        db.create_table(u'customer', (
            ('customer_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('store', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rentals.Store'])),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['addresses.Address'])),
            ('activebool', self.gf('django.db.models.fields.BooleanField')()),
            ('create_date', self.gf('django.db.models.fields.DateField')()),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('active', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'rentals', ['Customer'])

        # Adding model 'Inventory'
        db.create_table(u'inventory', (
            ('inventory_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('film', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['films.Film'])),
            ('store', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rentals.Store'])),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'rentals', ['Inventory'])

        # Adding model 'Rental'
        db.create_table(u'rental', (
            ('rental_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('rental_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('inventory', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rentals.Inventory'])),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rentals.Customer'])),
            ('return_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('staff', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rentals.Staff'])),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'rentals', ['Rental'])

        # Adding model 'Payment'
        db.create_table(u'payment', (
            ('payment_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rentals.Customer'])),
            ('staff', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rentals.Staff'])),
            ('rental', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rentals.Rental'])),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('payment_date', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'rentals', ['Payment'])

        # Adding model 'Staff'
        db.create_table(u'staff', (
            ('staff_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=45)),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['addresses.Address'])),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('store', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['rentals.Store'])),
            ('active', self.gf('django.db.models.fields.BooleanField')()),
            ('username', self.gf('django.db.models.fields.CharField')(max_length=16)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('picture', self.gf('django.db.models.fields.BinaryField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'rentals', ['Staff'])

        # Adding model 'Store'
        db.create_table(u'store', (
            ('store_id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('manager_staff', self.gf('django.db.models.fields.related.ForeignKey')(related_name=u'store_managed_by_me', unique=True, to=orm['rentals.Staff'])),
            ('address', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['addresses.Address'])),
            ('last_update', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'rentals', ['Store'])


    def backwards(self, orm):
        # Deleting model 'Customer'
        db.delete_table(u'customer')

        # Deleting model 'Inventory'
        db.delete_table(u'inventory')

        # Deleting model 'Rental'
        db.delete_table(u'rental')

        # Deleting model 'Payment'
        db.delete_table(u'payment')

        # Deleting model 'Staff'
        db.delete_table(u'staff')

        # Deleting model 'Store'
        db.delete_table(u'store')


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
        },
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
        },
        u'rentals.customer': {
            'Meta': {'object_name': 'Customer', 'db_table': "u'customer'"},
            'active': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'activebool': ('django.db.models.fields.BooleanField', [], {}),
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['addresses.Address']"}),
            'create_date': ('django.db.models.fields.DateField', [], {}),
            'customer_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'store': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rentals.Store']"})
        },
        u'rentals.inventory': {
            'Meta': {'object_name': 'Inventory', 'db_table': "u'inventory'"},
            'film': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['films.Film']"}),
            'inventory_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'store': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rentals.Store']"})
        },
        u'rentals.payment': {
            'Meta': {'object_name': 'Payment', 'db_table': "u'payment'"},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rentals.Customer']"}),
            'payment_date': ('django.db.models.fields.DateTimeField', [], {}),
            'payment_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rental': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rentals.Rental']"}),
            'staff': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rentals.Staff']"})
        },
        u'rentals.rental': {
            'Meta': {'object_name': 'Rental', 'db_table': "u'rental'"},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rentals.Customer']"}),
            'inventory': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rentals.Inventory']"}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'rental_date': ('django.db.models.fields.DateTimeField', [], {}),
            'rental_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'return_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'staff': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rentals.Staff']"})
        },
        u'rentals.staff': {
            'Meta': {'object_name': 'Staff', 'db_table': "u'staff'"},
            'active': ('django.db.models.fields.BooleanField', [], {}),
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['addresses.Address']"}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '45'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'picture': ('django.db.models.fields.BinaryField', [], {'null': 'True', 'blank': 'True'}),
            'staff_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'store': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['rentals.Store']"}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        },
        u'rentals.store': {
            'Meta': {'object_name': 'Store', 'db_table': "u'store'"},
            'address': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['addresses.Address']"}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'manager_staff': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'store_managed_by_me'", 'unique': 'True', 'to': u"orm['rentals.Staff']"}),
            'store_id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['rentals']