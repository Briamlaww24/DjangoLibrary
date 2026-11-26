from django import forms

from catalog.models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ("name", "biography")
        widgets = {"biography": forms.Textarea(attrs={"rows": 4})}

    def clean_name(self):
        return " ".join(self.cleaned_data["name"].split())
