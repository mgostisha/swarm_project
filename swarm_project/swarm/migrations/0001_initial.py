# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DragConditions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('drag_option', models.BooleanField(default=False)),
                ('vel_field', models.CharField(default=b'ZV', max_length=2, choices=[(b'ZV', b'Zero Velocity'), (b'MP', b'Match Potential'), (b'RO', b'Radial Outflow')])),
                ('RO_initial_vel', models.FloatField(default=0.0, help_text=b'km/s')),
                ('RO_r_scale', models.FloatField(default=0.0, help_text=b'kpc')),
                ('den_field', models.CharField(default=b'CD', max_length=2, choices=[(b'CD', b'Constant Density'), (b'PL', b'Power Law'), (b'DD', b'Density Disks')])),
                ('CD_density', models.FloatField(default=-3.0, help_text=b'log particles/cm^3')),
                ('PL_density', models.FloatField(default=-3.0, help_text=b'log particles/cm^3')),
                ('PL_r_scale', models.FloatField(default=0.0, help_text=b'kpc')),
                ('PL_alpha_exp', models.FloatField(default=0.0, help_text=b'')),
                ('DD_density1', models.FloatField(default=0.0, help_text=b'log particles/cm^3')),
                ('DD_density2', models.FloatField(default=0.0, help_text=b'log particles/cm^3')),
                ('DD_density3', models.FloatField(default=0.0, help_text=b'log particles/cm^3')),
                ('DD_r_scale1', models.FloatField(default=0.0, help_text=b'kpc')),
                ('DD_r_scale2', models.FloatField(default=0.0, help_text=b'kpc')),
                ('DD_r_scale3', models.FloatField(default=0.0, help_text=b'kpc')),
                ('DD_z_scale1', models.FloatField(default=0.0, help_text=b'kpc')),
                ('DD_z_scale2', models.FloatField(default=0.0, help_text=b'kpc')),
                ('DD_z_scale3', models.FloatField(default=0.0, help_text=b'kpc')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InitialConditions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('x_coord', models.FloatField(default=0.0, help_text=b'kpc')),
                ('y_coord', models.FloatField(default=-8.0, help_text=b'kpc')),
                ('z_coord', models.FloatField(default=0.0, help_text=b'kpc')),
                ('vx_vel', models.FloatField(default=220.0, help_text=b'km/s')),
                ('vy_vel', models.FloatField(default=0.0, help_text=b'km/s')),
                ('vz_vel', models.FloatField(default=0.0, help_text=b'km/s')),
                ('column_density', models.FloatField(default=20.0, help_text=b'log particles/cm^2')),
                ('sigma_coord', models.FloatField(default=0.1, help_text=b'kpc')),
                ('sigma_vel', models.FloatField(default=0.1, help_text=b'km/s')),
                ('sigma_col_den', models.FloatField(default=1.0, help_text=b'log particles/cm^2')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='dragconditions',
            name='initial_conditions',
            field=models.OneToOneField(to='swarm.InitialConditions'),
            preserve_default=True,
        ),
    ]
