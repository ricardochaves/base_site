from django.shortcuts import render

from htmlmin.decorators import minified_response
# Create your views here.

# @requires_csrf_token


@minified_response
def index(request):

    return render(request, 'mainapp/index.html')
