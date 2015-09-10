# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0002_auto_20150909_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='slug',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
