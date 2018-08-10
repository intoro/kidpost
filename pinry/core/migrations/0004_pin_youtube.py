# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20180804_0629'),
    ]

    operations = [
        migrations.AddField(
            model_name='pin',
            name='youtube',
            field=models.TextField(null=True, blank=True),
        ),
    ]
