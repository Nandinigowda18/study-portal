from django.contrib import admin
from . models import *

# Register your models here.
admin.site.register(Notes)

#homework section

admin.site.register(Homework)

#todo section

admin.site.register(Todo)
