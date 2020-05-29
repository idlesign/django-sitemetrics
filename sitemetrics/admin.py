from django.contrib import admin

from .models import Keycode


@admin.register(Keycode)
class KeycodeAdmin(admin.ModelAdmin):

    list_display = (
        'site',
        'provider',
        'keycode',
        'active',
    )

    list_editable = (
        'active',
    )

    search_fields = [
        'keycode',
    ]

    list_filter = [
        'site',
        'provider',
        'active',
    ]

    ordering = ['site']
