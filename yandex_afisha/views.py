from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def show_index(request):
    # template = loader.get_template()
    return render(request, 'index.html')
