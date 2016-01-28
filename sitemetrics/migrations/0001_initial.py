# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keycode',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('provider', models.CharField(max_length=50, verbose_name='Provider', choices=[('yandex', 'Yandex Metrika'), ('google', 'Google Analytics'), ('openstat', 'Openstat')], help_text='Metrics service provider name.')),
                ('keycode', models.CharField(max_length=80, verbose_name='Keycode', help_text='Keycode or identifier given by metrics service provider for site(s).')),
                ('active', models.BooleanField(default=True, verbose_name='Active', help_text='Whether this keycode is available to use.')),
                ('site', models.ForeignKey(verbose_name='Site', help_text='Site for which metrics keycode is registered.', to='sites.Site')),
            ],
            options={
                'verbose_name': 'Keycode',
                'verbose_name_plural': 'Keycodes',
            },
        ),
    ]
