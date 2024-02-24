from django.db import models

# Create your models here.
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    revenue = models.CharField(max_length=100, null=True, blank=True)

    description = models.TextField()
    image = models.ImageField(upload_to='movie_images/', null=True, blank=True)

    year = models.IntegerField()

    def __str__(self):
        return self.title
