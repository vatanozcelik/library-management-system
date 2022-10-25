from django.views.generic import ListView
from core.models import Book


class BookList(ListView):
    model = Book
    template_name = "core/home.html"
