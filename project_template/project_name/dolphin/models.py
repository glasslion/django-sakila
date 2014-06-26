# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Actor(models.Model):
    actor_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    last_update = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'actor'


class Address(models.Model):
    address_id = models.IntegerField(primary_key=True)
    address = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, blank=True)
    district = models.CharField(max_length=20)
    city = models.ForeignKey('City')
    postal_code = models.CharField(max_length=10, blank=True)
    phone = models.CharField(max_length=20)
    last_update = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'address'


class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=25)
    last_update = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'category'

class City(models.Model):
    city_id = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=50)
    country = models.ForeignKey('Country')
    last_update = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'city'

class Country(models.Model):
    country_id = models.IntegerField(primary_key=True)
    country = models.CharField(max_length=50)
    last_update = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'country'

class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    store = models.ForeignKey('Store')
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=50, blank=True)
    address = models.ForeignKey(Address)
    activebool = models.BooleanField()
    create_date = models.DateField()
    last_update = models.DateTimeField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'customer'


class Film(models.Model):
    film_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    release_year = models.IntegerField(blank=True, null=True)
    language = models.ForeignKey('Language')
    original_language = models.ForeignKey('Language', blank=True, null=True, related_name='filmAsOriginalLanguage')
    rental_duration = models.SmallIntegerField()
    rental_rate = models.DecimalField(max_digits=4, decimal_places=2)
    length = models.SmallIntegerField(blank=True, null=True)
    replacement_cost = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.TextField(blank=True) # This field type is a guess.
    last_update = models.DateTimeField()
    special_features = models.TextField(blank=True) # This field type is a guess.
    fulltext = models.TextField() # This field type is a guess.
    class Meta:
        managed = False
        db_table = 'film'

class FilmActor(models.Model):
    actor = models.ForeignKey(Actor)
    film = models.ForeignKey(Film)
    last_update = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'film_actor'

class FilmCategory(models.Model):
    film = models.ForeignKey(Film)
    category = models.ForeignKey(Category)
    last_update = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'film_category'


class Inventory(models.Model):
    inventory_id = models.IntegerField(primary_key=True)
    film = models.ForeignKey(Film)
    store = models.ForeignKey('Store')
    last_update = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'inventory'

class Language(models.Model):
    language_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    last_update = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'language'


class Payment(models.Model):
    payment_id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey(Customer)
    staff = models.ForeignKey('Staff')
    rental = models.ForeignKey('Rental')
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    payment_date = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'payment'

class Rental(models.Model):
    rental_id = models.IntegerField(primary_key=True)
    rental_date = models.DateTimeField()
    inventory = models.ForeignKey(Inventory)
    customer = models.ForeignKey(Customer)
    return_date = models.DateTimeField(blank=True, null=True)
    staff = models.ForeignKey('Staff')
    last_update = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'rental'

class SouthMigrationhistory(models.Model):
    id = models.IntegerField(primary_key=True)
    app_name = models.CharField(max_length=255)
    migration = models.CharField(max_length=255)
    applied = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'south_migrationhistory'

class Staff(models.Model):
    staff_id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    address = models.ForeignKey(Address)
    email = models.CharField(max_length=50, blank=True)
    store = models.ForeignKey('Store')
    active = models.BooleanField()
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=40, blank=True)
    last_update = models.DateTimeField()
    picture = models.BinaryField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'staff'

class Store(models.Model):
    store_id = models.IntegerField(primary_key=True)
    manager_staff = models.ForeignKey(Staff, unique=True, related_name='store_managed_by_me')
    address = models.ForeignKey(Address)
    last_update = models.DateTimeField()
    class Meta:
        managed = False
        db_table = 'store'

