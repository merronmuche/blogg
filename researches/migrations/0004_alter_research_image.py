# Generated by Django 4.1.3 on 2022-11-08 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('researches', '0003_research_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='research',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
