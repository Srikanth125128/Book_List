from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length =255,default="unknown publisher")
    published_year = models.IntegerField(default=2019)


