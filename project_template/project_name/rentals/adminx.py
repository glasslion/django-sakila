import xadmin

from django.db.models import get_models, get_app

for model in get_models(get_app('rentals')):
    xadmin.site.register(model)