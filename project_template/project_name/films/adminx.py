import xadmin

from .models import Actor, Category, Film, Language

xadmin.site.register(Actor)
xadmin.site.register(Category)
xadmin.site.register(Film)
xadmin.site.register(Language)

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
xadmin.site.register(xadmin.views.BaseAdminView, BaseSetting)
