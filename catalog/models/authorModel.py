from django.db import models
from django.urls import reverse


class Author(models.Model):
    name = models.CharField("nombre", max_length=150, unique=True)
    biography = models.TextField("biografía", blank=True)

    class Meta:
        ordering = ("name", "pk")
        verbose_name = "autor"
        verbose_name_plural = "autores"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("catalog:author_detail", args=[self.pk])
