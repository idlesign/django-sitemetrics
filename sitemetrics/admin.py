from sitemetrics.models import Keycode
from django.contrib import admin

class KeycodeAdmin(admin.ModelAdmin):
    list_display = ('site', 'provider', 'keycode', 'active',)
    list_editable = ('active',)
    search_fields = ['keycode']
    list_filter = ['site', 'provider', 'active']
    ordering = ['site']

admin.site.register(Keycode, KeycodeAdmin)