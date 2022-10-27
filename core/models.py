from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    contributor = models.ManyToManyField(
        'Contributor', through='BookContributor')
    user = models.ManyToManyField(User, through='UserBook')
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class UserBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)


class Contributor(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class BookContributor(models.Model):
    class ContributorName(models.TextChoices):
        AUTHOR = "AUTHOR", "Author"
        CO_AUTHOR = "CO-AUTHOR", "Co-Author"
        EDITOR = "EDITOR", "Editor"

    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    contributor = models.ForeignKey('Contributor', on_delete=models.CASCADE)
    role = models.CharField(verbose_name="verbose name",
                            choices=ContributorName.choices, max_length=20)

    def __str__(self):
        return self.role
