import xadmin

from .models import Customer, Inventory, Rental, Payment, Staff,  Store


xadmin.site.register(Customer)
xadmin.site.register(Inventory)
xadmin.site.register(Rental)
xadmin.site.register(Payment)
xadmin.site.register(Staff)
xadmin.site.register(Store)
