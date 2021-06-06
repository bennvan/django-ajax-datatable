# Generated by Django 3.0.8 on 2021-06-05 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20200926_0912'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='url',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='artist',
            name='url',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='track',
            name='url',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
