# Generated by Django 5.0.3 on 2024-04-06 10:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('railway_line', models.CharField(max_length=100)),
                ('ring_number', models.IntegerField()),
                ('hostname', models.CharField(max_length=100)),
                ('btn_router_type', models.CharField(choices=[('7705-SAR-8', '7705-SAR-8'), ('7705-SAR-HC', '7705-SAR-HC')], max_length=100)),
                ('site_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('site_information', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bom_app.siteinformation')),
            ],
        ),
    ]
