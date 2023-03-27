from django.contrib import admin

# Register your models here.
from .models import Mascotas, Dueño

admin.site.register([Mascotas, Dueño])