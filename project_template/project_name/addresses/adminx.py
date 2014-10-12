import xadmin

from .models import Address, City, Country


xadmin.site.register(Address)
xadmin.site.register(City)
xadmin.site.register(Country)
