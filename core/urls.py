from django.urls import path
from core.views import BookList

urlpatterns = [
    path("", BookList.as_view(), name="book-list"),
]
