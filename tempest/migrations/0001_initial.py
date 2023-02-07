# Generated by Django 4.1.3 on 2022-11-14 10:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Clothing_bottom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Clothing_etc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Clothing_outer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Clothing_top',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('region', models.CharField(max_length=10)),
                ('baseDate', models.CharField(max_length=10)),
                ('baseTime', models.CharField(max_length=10)),
                ('json', jsonfield.fields.JSONField()),
            ],
        ),
        migrations.CreateModel(
            name='ClotheRecords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bottom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tempest.clothing_bottom')),
                ('etc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tempest.clothing_etc')),
                ('outer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tempest.clothing_outer')),
                ('top', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tempest.clothing_top')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('weather', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tempest.weather')),
            ],
        ),
    ]