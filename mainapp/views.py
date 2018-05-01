from django.shortcuts import render

from mainapp.models import ModelExample

from htmlmin.decorators import minified_response
# Create your views here.

# @requires_csrf_token


@minified_response
def index(request):
    examples = ModelExample.objects.filter(active=True)
    return render(request, 'mainapp/index.html', {'examples': examples, })
