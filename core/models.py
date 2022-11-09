from email.policy import default
from django.db import models
from django.contrib.auth.models import User


class Language(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class Contributor(models.Model):
    name = models.CharField(max_length=50, blank=True,
                            null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    contributor = models.ManyToManyField(
        Contributor, through='BookContributor')
    category = models.ManyToManyField(Category, through='BookCategory')
    user = models.ManyToManyField(User, through='UserBook')
    language = models.ForeignKey(
        Language, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    #  @admin.display(ordering='contributor__name', description='contributor')
    def get_contributor(self):
        return ", ".join([i.name for i in self.contributor.all()])

    # @admin.display(ordering='user__name', description='userbook')
    def get_user(self):
        return ", ".join([i.username for i in self.user.all()])


class UserBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(blank=True, null=True)


class BookCategory(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.book.title


class BookContributor(models.Model):
    class ContributorName(models.TextChoices):
        AUTHOR = "AUTHOR", "Author"
        CO_AUTHOR = "CO-AUTHOR", "Co-Author"
        EDITOR = "EDITOR", "Editor"

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    role = models.CharField(verbose_name="verbose name",
                            choices=ContributorName.choices, max_length=20)

    def __str__(self):
        return self.role
