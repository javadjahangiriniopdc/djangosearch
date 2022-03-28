from django.contrib import admin

# Register your models here.
from myapp.models import Person

admin.site.register(Person)