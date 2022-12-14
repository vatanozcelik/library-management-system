from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView

from core.models import Book, UserBook, Category
from core.serializers import BookSerializer


def home(request):
    books = Book.objects.all()
    bookCategories = Category.objects.all()
    context = {'books': books, 'bookCategories': bookCategories}
    return render(request, "core/home.html", context)

def category(request, slug):
    bookCategories = Category.objects.all()
    category = get_object_or_404(Category, slug=slug)
    books = Book.objects.filter(category=category.id)
    context = {
        'books': books,
        'bookCategories': bookCategories

    }
    return render(request, "core/department.html", context)


"""
class BookList(APIView):

    def get_object(self, request, pk):
        try:
            return Book.objects.get(pk=pk)
        except:
            raise Http404

    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        book = self.get_object(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

    def delete(self, request, pk):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""


class ListCreateView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class RetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'slug'


# def profile(request, pk):
#     user = get_object_or_404(User, pk=pk)
#     books = UserBook.objects.filter(user=user)
#     context = {
#         'books': books
#     }
#     return render(request, "core/profile.html", context)


class ProfileView(ListView):
    template_name = "core/profile.html"
    # queryset = UserBook.objects

    def get_queryset(self, pk):
        user_books = UserBook.objects.filter(user_id=pk)
        return user_books
