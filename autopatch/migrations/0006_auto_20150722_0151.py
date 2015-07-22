# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autopatch', '0005_auto_20150715_0142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='skip',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
    ]
