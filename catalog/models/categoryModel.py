from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField("nombre", max_length=100, unique=True)
    description = models.TextField("descripción", blank=True)

    class Meta:
        ordering = ("name", "pk")
        verbose_name = "categoría"
        verbose_name_plural = "categorías"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("catalog:category_detail", args=[self.pk])
