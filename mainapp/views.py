from django.shortcuts import render
from django.views.decorators.cache import cache_page

from mainapp.models import ModelExample

from htmlmin.decorators import minified_response

# @requires_csrf_token


@cache_page(30)
@minified_response
def index(request):
    examples = ModelExample.objects.filter(active=True)
    return render(request, 'mainapp/index.html', {'examples': examples, })
