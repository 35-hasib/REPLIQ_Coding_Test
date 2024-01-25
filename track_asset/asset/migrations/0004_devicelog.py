# Generated by Django 5.0.1 on 2024-01-25 16:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset', '0003_device'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkedout', models.DateTimeField()),
                ('return_checktime', models.DateTimeField()),
                ('check_condition', models.CharField(max_length=100)),
                ('return_check_condition', models.CharField(max_length=100)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.device')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asset.employee')),
            ],
        ),
    ]
