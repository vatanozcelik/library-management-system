from django.contrib import admin
from core.models import Book, BookContributor, Contributor


class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('title',)
    }


admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Contributor)
