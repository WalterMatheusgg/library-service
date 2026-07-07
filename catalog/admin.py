from django.contrib import admin

from catalog.models import Author, Book, Borrowing, Genre


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "date_of_birth")
    search_fields = ("first_name", "last_name")


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "inventory", "available_copies")
    list_filter = ("genres", "author")
    search_fields = ("title", "author__first_name", "author__last_name")


@admin.register(Borrowing)
class BorrowingAdmin(admin.ModelAdmin):
    list_display = ("book", "borrower", "borrowed_at", "due_date", "returned_at")
    list_filter = ("returned_at", "due_date")
    search_fields = ("book__title", "borrower__username")
