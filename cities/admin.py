from django.contrib import admin

from .models import City

class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "state",)

admin.site.register(City, CityAdmin)