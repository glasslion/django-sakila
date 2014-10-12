import xadmin

from django.db.models import get_models, get_app

for model in get_models(get_app('addresses')):
    xadmin.site.register(model)