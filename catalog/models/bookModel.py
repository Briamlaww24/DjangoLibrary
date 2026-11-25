from django.conf import settings
from django.db import models
from django.core.validators import FileExtensionValidator
class Book(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="uploaded_books",
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    genre = models.CharField(max_length=100)
    description = models.TextField()
    extract = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True,)
    pdf = models.FileField(upload_to="catalog/pdf/", null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    cover = models.ImageField(upload_to="catalog/covers/", null=True, blank=True)

    def __str__(self):
        return self.title
