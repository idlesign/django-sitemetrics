from django import forms
from django.contrib import admin

from .models import Keycode
from .utils import get_provider_choices


class KeycodeForm(forms.ModelForm):
    """Keycode admin form with provider choices resolved at render time."""

    class Meta:
        model = Keycode
        fields = '__all__'
        widgets = {
            'provider': forms.Select(choices=get_provider_choices),
        }


@admin.register(Keycode)
class KeycodeAdmin(admin.ModelAdmin):

    form = KeycodeForm

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
