from datetime import datetime

from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

from myapp.forms import SearchForm
from myapp.models import Person


def home(request):
    persons = Person.objects.all()
    form = SearchForm()

    if 'search' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            cd = form.cleaned_data['search']
            persons= persons.filter(Q(name__icontains=cd) | Q(description__icontains=cd))

    return render(request, 'myapp/index.html', {'persons': persons, 'form': form})
