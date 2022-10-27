from django.contrib import admin
from core.models import (
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
        'get_contributor'
    )

    @admin.display(ordering='book__contributor', description='Book')
    def get_contributor(self, obj):
        return obj.book.contributor


admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor, BookContributorAdmin)
admin.site.register(Contributor)
admin.site.register(UserBook)
