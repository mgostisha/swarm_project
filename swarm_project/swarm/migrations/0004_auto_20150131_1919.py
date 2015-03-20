# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('swarm', '0003_simulationparameters'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dragconditions',
            name='initial_conditions',
        ),
        migrations.DeleteModel(
            name='DragConditions',
        ),
        migrations.RemoveField(
            model_name='simulationparameters',
            name='initial_conditions',
        ),
        migrations.DeleteModel(
            name='InitialConditions',
        ),
        migrations.AddField(
            model_name='simulationparameters',
            name='CD_density',
            field=models.FloatField(default=-3.0, help_text=b'log particles/cm^2'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='simulationparameters',
            name='DD_density1',
            field=models.FloatField(default=0.0, help_text=b'log particles/cm^2'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='simulationparameters',
            name='DD_density2',
            field=models.FloatField(default=0.0, help_text=b'log particles/cm^2'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='simulationparameters',
            name='DD_density3',
            field=models.FloatField(default=0.0, help_text=b'log particles/cm^2'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='simulationparameters',
            name='DD_r_scale1',
            field=models.FloatField(default=0.0, help_text=b'kpc'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='simulationparameters',
            name='DD_r_scale2',
            field=models.FloatField(default=0.0, help_text=b'kpc'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='simulationparameters',
            name='DD_r_scale3',
            field=models.FloatField(default=0.0, help_text=b'kpc'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='simulationparameters',
            name='DD_z_scale1',
            field=models.FloatField(default=0.0, help_text=b'kpc'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='simulationparameters',
            name='DD_z_scale2',
            field=models.FloatField(default=0.0, help_text=b'kpc'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='simulationparameters',
            name='DD_z_scale3',
            field=models.FloatField(default=0.0, help_text=b'kpc'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='simulationparameters',
            name='PL_alpha_exp',
            field=models.FloatField(default=0.0, help_text=b''),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='simulationparameters',
            name='PL_density',
            field=models.FloatField(default=-3.0, help_text=b'log particles/cm^2'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='simulationparameters',
            name='PL_r_scale',
            field=models.FloatField(default=0.0, help_text=b'kpc'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='simulationparameters',
            name='RO_initial_vel',
            field=models.FloatField(default=0.0, help_text=b'km/s'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='simulationparameters',
            name='RO_r_scale',
            field=models.FloatField(default=0.0, help_text=b'kpc'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='simulationparameters',
            name='column_density',
            field=models.FloatField(default=20.0, help_text=b'log particles/cm^2'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='simulationparameters',
            name='den_field',
            field=models.CharField(default=b'CD', max_length=2, choices=[(b'CD', b'Constant Density'), (b'PL', b'Power Law'), (b'DD', b'Density Disks')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='simulationparameters',
            name='drag_option',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='simulationparameters',
            name='sigma_col_den',
            field=models.FloatField(default=1.0, help_text=b'log particles/cm^2'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='simulationparameters',
            name='sigma_coord',
            field=models.FloatField(default=0.1, help_text=b'kpc'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='simulationparameters',
            name='sigma_vel',
            field=models.FloatField(default=0.1, help_text=b'km/s'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='simulationparameters',
            name='vel_field',
            field=models.CharField(default=b'ZV', max_length=2, choices=[(b'ZV', b'Zero Velocity'), (b'MP', b'Match Potential'), (b'RO', b'Radial Outflow')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='simulationparameters',
            name='vx_vel',
            field=models.FloatField(default=220.0, help_text=b'km/s'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='simulationparameters',
            name='vy_vel',
            field=models.FloatField(default=0.0, help_text=b'km/s'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='simulationparameters',
            name='vz_vel',
            field=models.FloatField(default=0.0, help_text=b'km/s'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='simulationparameters',
            name='x_coord',
            field=models.FloatField(default=0.0, help_text=b'kpc'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='simulationparameters',
            name='y_coord',
            field=models.FloatField(default=-8.0, help_text=b'kpc'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='simulationparameters',
            name='z_coord',
            field=models.FloatField(default=0.0, help_text=b'kpc'),
            preserve_default=True,
        ),
    ]
