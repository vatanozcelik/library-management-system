from django.contrib import admin
from core.models import (
    BookCategory,
    Language,
    Category,
    Book,
    BookContributor,
    Contributor,
    UserBook,
)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }


class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'get_contributor', 'get_user', 'get_language'
    )
    prepopulated_fields = {
        'slug': ('title',)
    }

    @admin.display()
    def get_language(self, obj):
        return obj.language.name


class BookContributorAdmin(admin.ModelAdmin):
    list_display = (
        'book', 'get_contributor', 'role'
    )

    @admin.display(ordering='contributor__name', description='contributor')
    def get_contributor(self, obj):
        return obj.contributor.name


class UserBookAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'book', 'quantity'
    )


"""   SINCE ATTRIBUTES ARE FOREIGN KEYS THEN DO NOT NEED ANYMORE   """
# def get_users(self, obj):
#     return ", ".join([str(i) for i in obj.user.all()])


class BookCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'category', 'book',
    )


"""   SINCE ATTRIBUTES ARE FOREIGN KEYS THEN DO NOT NEED ANYMORE """
# @admin.display(ordering='book__title', description='Book')
# def get_name(self, obj):
#     return obj.book.title


admin.site.register(Contributor)
admin.site.register(Language)
admin.site.register(Category, CategoryAdmin)
admin.site.register(UserBook, UserBookAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookCategory, BookCategoryAdmin)
admin.site.register(BookContributor, BookContributorAdmin)
