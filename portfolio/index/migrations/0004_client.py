# Generated by Django 4.1.3 on 2022-11-23 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_alter_slider_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=400)),
                ('image', models.ImageField(upload_to='client/', verbose_name='')),
            ],
        ),
    ]
