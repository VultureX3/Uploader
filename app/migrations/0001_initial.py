# Generated by Django 3.0.5 on 2020-04-19 22:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('upload', models.FileField(upload_to='/')),
                ('profile',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,
                                   related_name='files',
                                   to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]