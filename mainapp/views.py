from django.shortcuts import render
from django.views.decorators.cache import cache_page
from htmlmin.decorators import minified_response
from mainapp.models import ModelExample


@cache_page(30)
@minified_response
def index(request):
    examples = ModelExample.objects.filter(active=True)
    return render(request, "mainapp/index.html", {"examples": examples})
