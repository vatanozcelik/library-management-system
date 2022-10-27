from django.urls import path
from core.views import ListCreateView

urlpatterns = [
    path("", ListCreateView.as_view(), name="book-list-create"),
]
