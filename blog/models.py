from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    blog_date = models.DateTimeField()
