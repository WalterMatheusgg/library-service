from django.contrib import admin

from catalog.models import Author, Book, Borrowing, Genre


admin.site.site_header = "Administração da Biblioteca Digital"
admin.site.site_title = "Biblioteca Digital"
admin.site.index_title = "Painel administrativo"


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "date_of_birth")
    list_display_links = ("first_name", "last_name")
    search_fields = ("first_name", "last_name")
    ordering = ("last_name", "first_name")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "inventory",
        "available_copies_display",
    )
    list_display_links = ("title",)
    list_filter = ("genres", "author")
    search_fields = ("title", "author__first_name", "author__last_name")
    filter_horizontal = ("genres",)

    @admin.display(description="Disponíveis")
    def available_copies_display(self, obj):
        return obj.available_copies


@admin.register(Borrowing)
class BorrowingAdmin(admin.ModelAdmin):
    list_display = (
        "book",
        "borrower",
        "borrowed_at",
        "due_date",
        "returned_at",
        "status_display",
    )
    list_filter = ("returned_at", "due_date")
    search_fields = ("book__title", "borrower__username")
    date_hierarchy = "borrowed_at"

    @admin.display(description="Status")
    def status_display(self, obj):
        if obj.returned_at:
            return "Devolvido"
        return "Ativo"
