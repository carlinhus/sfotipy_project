# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0003_album_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='slug',
            field=models.CharField(default=datetime.datetime(2015, 9, 10, 8, 20, 10, 141441, tzinfo=utc), max_length=255, blank=True),
            preserve_default=False,
        ),
    ]
