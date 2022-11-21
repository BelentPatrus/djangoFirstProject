from django.db import models

# Create your models here.

# table name


class about(models.Model):
    # table field names
    title = models.CharField(max_length=50, blank=False)
    description = models.TextField(max_length=800, blank=False)
    image = models.ImageField((""), upload_to='about/', blank=False)
