# Generated by Django 3.2.1 on 2021-05-14 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_keyword'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='keywords',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='website',
            name='storage_url',
            field=models.URLField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='website',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='website',
            name='url',
            field=models.URLField(blank=True, max_length=255, unique=True),
        ),
    ]
