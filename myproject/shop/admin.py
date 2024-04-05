from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Shop)
class co_ntactform(admin.ModelAdmin):
    list_display = ('id','name','lastname','latitude','longitude')