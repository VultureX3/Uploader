# Generated by Django 3.0.5 on 2020-04-19 22:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='upload',
            field=models.FileField(upload_to='files/'),
        ),
    ]