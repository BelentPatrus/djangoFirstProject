# Generated by Django 4.1.3 on 2022-11-23 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_slider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(upload_to='slider/', verbose_name=''),
        ),
    ]
