# Generated by Django 4.1.2 on 2022-10-27 15:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0003_category_language_remove_book_user_bookcategory_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="user",
            field=models.ManyToManyField(
                through="core.UserBook", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
