# Generated by Django 4.1.3 on 2022-11-08 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('researches', '0005_alter_research_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='research',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='researches/static/images'),
        ),
    ]
