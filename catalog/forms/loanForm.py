from django import forms

from catalog.models import Loan


class LoanForm(forms.ModelForm):
    class Meta:
        model = Loan
        fields = ("book", "borrower", "borrowed_on", "due_on", "status")
        widgets = {
            "borrowed_on": forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
            "due_on": forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}),
        }

    def clean_due_on(self):
        dueOn = self.cleaned_data["due_on"]
        borrowedOn = self.cleaned_data.get("borrowed_on")
        if borrowedOn and dueOn < borrowedOn:
            raise forms.ValidationError("La devolución debe ser igual o posterior al préstamo.")
        return dueOn
