from django.urls import path

from catalog import views

urlpatterns = [
    path("", views.loanList, name="loan_list"),
    path("<int:pk>/", views.loanDetail, name="loan_detail"),
]
