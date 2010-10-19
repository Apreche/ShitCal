from django.contrib import admin

from shitcal.models import Shit

class ShitAdmin(admin.ModelAdmin):
    raw_id_fields = ('user',)

admin.site.register(Shit, ShitAdmin)
