# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_pin_description_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pin',
            name='origin',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='pin',
            name='url',
            field=models.URLField(null=True, blank=True),
        ),
    ]
