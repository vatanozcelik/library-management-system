from dataclasses import fields
from rest_framework.serializers import ModelSerializer
from core.models import (
    Book,
    Contributor,
    UserBook,
)


class ContributorSerializer(ModelSerializer):
    class Meta:
        model = Contributor
        fields = (
            'name',
        )


class UserBookSerializer(ModelSerializer):
    class Meta:
        model = UserBook
        fields = (
            'user',
        )


class BookSerializer(ModelSerializer):
    contributor = ContributorSerializer(read_only=True, many=True)
    user = UserBookSerializer(read_only=True, many=True)

    class Meta:
        model = Book
        fields = (
            'id', 'title', 'slug', 'contributor', 'description', 'user'
        )
        lookup_field = 'slug'
