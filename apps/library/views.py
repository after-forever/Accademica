from django.shortcuts import render
from django.views.generic import ListView
from django.views import generic
from collection.models import Collection

class IndexView(ListView):
    template_name = "index.html"
    context_object_name = 'collection_list'
    model = Collection