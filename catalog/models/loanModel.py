from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Loan(models.Model):
    class Status(models.TextChoices):
        ACTIVE = "active", "Activo"
        RETURNED = "returned", "Devuelto"

    book = models.ForeignKey("Book", on_delete=models.PROTECT, related_name="loans", verbose_name="libro")
    borrower = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="loans", verbose_name="lector",
    )
    borrowed_on = models.DateField("fecha de préstamo", default=timezone.localdate)
    due_on = models.DateField("fecha de devolución")
    status = models.CharField("estado", max_length=10, choices=Status, default=Status.ACTIVE)

    class Meta:
        ordering = ("-borrowed_on", "-pk")
        verbose_name = "préstamo"
        verbose_name_plural = "préstamos"
        constraints = [
            models.CheckConstraint(
                condition=models.Q(due_on__gte=models.F("borrowed_on")),
                name="catalog_loan_due_after_start",
            ),
        ]

    def __str__(self):
        return f"{self.book} · {self.borrower}"

    def get_absolute_url(self):
        return reverse("catalog:loan_detail", args=[self.pk])
