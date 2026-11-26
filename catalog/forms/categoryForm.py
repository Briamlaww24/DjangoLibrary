from django import forms

from catalog.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ("name", "description")
        widgets = {"description": forms.Textarea(attrs={"rows": 4})}

    def clean_name(self):
        return " ".join(self.cleaned_data["name"].split())
