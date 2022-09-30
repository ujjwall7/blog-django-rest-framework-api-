from django.contrib import admin
from .models import *

@admin.register(Blog)
class blogdisplay(admin.ModelAdmin):
    list_display = ['Title','Description','user','Author','Image']