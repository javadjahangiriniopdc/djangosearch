from datetime import datetime

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect

from myapp.models import Person


@csrf_protect
def home(request):
    persons = Person.objects.all()
    if 'search' in request.GET:
        key = request.GET.get('search')
        persons = Person.objects.all().filter(Q(name__icontains=key), Q(description__icontains=key))
    else:
        persons = Person.objects.all()

    return render(request, 'myapp/index.html', {'persons': persons})



