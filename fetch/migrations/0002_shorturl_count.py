# Generated by Django 2.0.1 on 2018-03-17 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fetch', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shorturl',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]
