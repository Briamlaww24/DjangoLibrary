from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, render
from django.views.decorators.cache import never_cache

from catalog.models import Loan


@never_cache
@login_required
@permission_required("catalog.view_loan", raise_exception=True)
def loanList(request):
    loans = Loan.objects.select_related("book", "borrower")
    return render(request, "catalog/loans/list.html", {"loans": loans})


@never_cache
@login_required
@permission_required("catalog.view_loan", raise_exception=True)
def loanDetail(request, pk):
    loan = get_object_or_404(Loan.objects.select_related("book", "borrower"), pk=pk)
    return render(request, "catalog/loans/detail.html", {"loan": loan})
