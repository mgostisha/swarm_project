# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swarm', '0002_auto_20150128_2233'),
    ]

    operations = [
        migrations.CreateModel(
            name='SimulationParameters',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('potential', models.CharField(default=b'WF', max_length=2, choices=[(b'PS', b'Point Source'), (b'WF', b'Wolfire')])),
                ('PS_mass', models.FloatField(default=4.0, help_text=b'log M_sun')),
                ('WF_disk', models.BooleanField(default=True)),
                ('WF_bulge', models.BooleanField(default=True)),
                ('WF_halo', models.BooleanField(default=True)),
                ('total_time', models.FloatField(default=1.0, help_text=b'Gyr')),
                ('timesteps', models.IntegerField(default=1000, help_text=b'')),
                ('n_particles', models.IntegerField(default=5, help_text=b'')),
                ('int_con_tol', models.FloatField(default=-3.0, help_text=b'log pc')),
                ('email_address', models.EmailField(max_length=75)),
                ('initial_conditions', models.ForeignKey(to='swarm.InitialConditions')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
