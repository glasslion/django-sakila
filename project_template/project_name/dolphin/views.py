from __future__ import absolute_import

from django.http import HttpResponse
from django.views.generic import TemplateView, ListView
from .models import Film

class FilmListView(ListView):
    model = Film