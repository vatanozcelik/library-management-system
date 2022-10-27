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


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }


class BookContributorAdmin(admin.ModelAdmin):
    list_display = (
        'book', 'contributor', 'role'
    )


class UserBookAdmin(admin.ModelAdmin):
    list_display = (
        'get_contributor',
    )

    @admin.display(ordering='contributor__name', description='Book')
    def get_contributor(self, obj):
        return obj.contributor.name


class BookCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'get_name',
    )

    @admin.display(ordering='book__title', description='Book')
    def get_name(self, obj):
        return obj.book.title


admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor, BookContributorAdmin)
admin.site.register(Contributor)
admin.site.register(UserBook, UserBookAdmin)
admin.site.register(Language)
admin.site.register(Category)
admin.site.register(BookCategory, BookCategoryAdmin)
