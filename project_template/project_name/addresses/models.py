from __future__ import unicode_literals

from django.db import models


class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, blank=True)
    district = models.CharField(max_length=20)
    city = models.ForeignKey('City')
    postal_code = models.CharField(max_length=10, blank=True)
    phone = models.CharField(max_length=20)
    last_update = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s %s, tel: %s' % (self.address, self.address2, self.phone)

    class Meta:
        db_table = 'address'


class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=50)
    country = models.ForeignKey('Country')
    last_update = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s, %s' % (self.city, self.country)

    class Meta:
        db_table = 'city'


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    country = models.CharField(max_length=50)
    last_update = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s' % self.country

    class Meta:
        db_table = 'country'
