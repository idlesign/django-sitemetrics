# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keycode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('provider', models.CharField(help_text='Metrics service provider name.', max_length=50, verbose_name='Provider', choices=[(b'yandex', 'Yandex Metrika'), (b'google', 'Google Analytics')])),
                ('keycode', models.CharField(help_text='Keycode or identifier given by metrics service provider for site(s).', max_length=80, verbose_name='Keycode')),
                ('active', models.BooleanField(default=True, help_text='Whether this keycode is available to use.', verbose_name='Active')),
                ('site', models.ForeignKey(verbose_name='Site', to='sites.Site', help_text='Site for which metrics keycode is registered.')),
            ],
            options={
                'verbose_name': 'Keycode',
                'verbose_name_plural': 'Keycodes',
            },
            bases=(models.Model,),
        ),
    ]
