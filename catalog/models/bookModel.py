from django.conf import settings
from django.db import models
from django.urls import reverse
from django.core.validators import FileExtensionValidator


class Book(models.Model):
    authors = models.ManyToManyField("Author", related_name="books", blank=True, verbose_name="autores")
    category = models.ForeignKey(
        "Category", on_delete=models.PROTECT, related_name="books",
        null=True, blank=True, verbose_name="categoría",
    )
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

    class Meta:
        ordering = ("title", "pk")
        verbose_name = "libro"
        verbose_name_plural = "libros"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("catalog:token", args=[self.slug])
