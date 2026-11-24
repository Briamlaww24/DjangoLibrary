from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    genre = models.CharField(max_length=100)
    description = models.TextField()
    extract = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True,)

    def __str__(self):
        return self.title
