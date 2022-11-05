from django.urls import path
from core.views import (
    home,
    # profile,
    ProfileView,
    ListCreateView,
    RetrieveUpdateDestroyView,
)

urlpatterns = [
    path("", home),
    # path("profile/<int:pk>/", profile, name="profile"),
    path("profile/<str:pk>/", ProfileView.as_view(), name="profile"),
    path("list-create/", ListCreateView.as_view(), name="book-list-create"),
    path("retrive-update-delete/<slug:slug>", RetrieveUpdateDestroyView.as_view(),
         name="book-retrive-update-delete")
]
