from django.db import models

# Create your models here.

# table name

# steps to create a table and push it to admin
# create class like below
# then run pythong manage.py makemigrations
# then check migration folder
# after all good run
# python manage.py migrate
# then go to admin.py


class about(models.Model):
    # table field names
    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=800, blank=False)
    image = models.ImageField((""), upload_to='about/', blank=False)

    def __str__(self):
        return self.title


class slider(models.Model):
    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=800, blank=False)
    image = models.ImageField((""), upload_to='slider/', blank=False)

    def __str__(self):
        return self.title


class client(models.Model):
    name = models.CharField(max_length=100, blank=False)
    link = models.CharField(max_length=400, blank=False)
    image = models.ImageField((""), upload_to='client/', blank=False)

    def __str__(self):
        return self.name
