from django.db import models

# Create your models here.
class ShortUrl(models.Model):
    url = models.URLField(max_length=2000)
    slug = models.SlugField(max_length=10)