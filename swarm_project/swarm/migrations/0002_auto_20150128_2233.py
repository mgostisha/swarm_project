# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swarm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dragconditions',
            name='initial_conditions',
            field=models.ForeignKey(to='swarm.InitialConditions'),
            preserve_default=True,
        ),
    ]
