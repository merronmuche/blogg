# Generated by Django 4.1.3 on 2022-11-08 11:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('researches', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='research',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
