from django import forms
from django.core.validators import FileExtensionValidator

from catalog.models.bookModel import Book

class BookCreationForm(forms.ModelForm):
    pdf = forms.FileField(
        required=True,
        label="Archivo PDF",
        validators=[FileExtensionValidator(allowed_extensions=['pdf'])],
    )
    cover = forms.ImageField(
        required=True,
        label="Portada",
    )
    
    class Meta:
        model = Book
        fields = ["title", "slug", "genre", "description", "extract", "rating", "pdf", "cover"]
        labels = {
            "title": "Título",
            "slug": "Slug",
            "genre": "Género",
            "description": "Descripción",
            "extract": "Extracto",
            "rating": "Calificación",
            "pdf": "PDF",
            "cover": "Portada",
        }

    def clean_slug(self):
        slug = self.cleaned_data["slug"]
        if slug == "create":
            raise forms.ValidationError(
                "El slug «create» está reservado. Elige otro, como «mi-libro»."
            )
        return slug
