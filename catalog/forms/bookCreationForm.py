from django import forms
from django.core.validators import FileExtensionValidator

from catalog.models import Book

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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk is not None:
            self.fields["slug"].disabled = True
            for name in ("pdf", "cover"):
                self.fields[name].required = False
                self.fields[name].widget = forms.FileInput()
                self.fields[name].help_text = "Deja este campo vacío para conservar el archivo actual."

    class Meta:
        model = Book
        fields = ["title", "slug", "genre", "description", "extract", "rating", "category", "authors", "pdf", "cover"]
        widgets = {
            "description": forms.Textarea(attrs={"rows": 5}),
            "extract": forms.Textarea(attrs={"rows": 4}),
        }
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
