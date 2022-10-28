from django.urls import path
from core.views import (
    ListCreateView,
    RetrieveUpdateDestroyView,
)

urlpatterns = [
    path("list-create/", ListCreateView.as_view(), name="book-list-create"),
    path("retrive-update-delete/<slug:slug>", RetrieveUpdateDestroyView.as_view(),
         name="book-retrive-update-delete")
]
