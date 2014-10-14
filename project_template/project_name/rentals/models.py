from __future__ import unicode_literals

from django.db import models

from addresses.models import Address
from films.models import Film


class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    store = models.ForeignKey('Store')
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=50, blank=True)
    address = models.ForeignKey(Address)
    activebool = models.BooleanField()
    create_date = models.DateField()
    last_update = models.DateTimeField(blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    class Meta:
        db_table = 'customer'


class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    film = models.ForeignKey(Film)
    store = models.ForeignKey('Store')
    last_update = models.DateTimeField()

    def __unicode__(self):
        return u'No.%d' % self.inventory_id

    class Meta:
        db_table = 'inventory'


class Rental(models.Model):
    rental_id = models.AutoField(primary_key=True)
    rental_date = models.DateTimeField()
    inventory = models.ForeignKey(Inventory)
    customer = models.ForeignKey(Customer)
    return_date = models.DateTimeField(blank=True, null=True)
    staff = models.ForeignKey('Staff')
    last_update = models.DateTimeField()

    def __unicode__(self):
        return u'No.%d' % self.rental_id

    class Meta:
        db_table = 'rental'


class Payment(models.Model):
    payment_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer)
    staff = models.ForeignKey('Staff')
    rental = models.ForeignKey('Rental')
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    payment_date = models.DateTimeField()

    def __unicode__(self):
        return u'%s' % self.payment_id

    class Meta:
        db_table = 'payment'


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
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

    def __unicode__(self):
        return u'%s %s (%s)' % (self.first_name, self.last_name, self.username)

    class Meta:
        db_table = 'staff'


class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    manager_staff = models.ForeignKey(
        Staff, unique=True, related_name='store_managed_by_me'
    )
    address = models.ForeignKey(Address)
    last_update = models.DateTimeField()

    def __unicode__(self):
        return u'No.%d' % self.store_id

    class Meta:
        db_table = 'store'
