# Generated by Django 3.2.3 on 2021-05-25 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_remove_moviemodel_keyword'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviemodel',
            name='keyword',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
