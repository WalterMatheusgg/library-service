from django.urls import path

from catalog import views

app_name = "catalog"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),

    path("books/", views.BookListView.as_view(), name="book-list"),
    path("books/create/", views.BookCreateView.as_view(), name="book-create"),
    path("books/<int:pk>/", views.BookDetailView.as_view(), name="book-detail"),
    path("books/<int:pk>/update/", views.BookUpdateView.as_view(), name="book-update"),
    path("books/<int:pk>/delete/", views.BookDeleteView.as_view(), name="book-delete"),
    path("books/<int:pk>/borrow/", views.BorrowBookView.as_view(), name="book-borrow"),

    path("authors/", views.AuthorListView.as_view(), name="author-list"),
    path("authors/create/", views.AuthorCreateView.as_view(), name="author-create"),
    path("authors/<int:pk>/", views.AuthorDetailView.as_view(), name="author-detail"),
    path("authors/<int:pk>/update/", views.AuthorUpdateView.as_view(), name="author-update"),
    path("authors/<int:pk>/delete/", views.AuthorDeleteView.as_view(), name="author-delete"),

    path("genres/", views.GenreListView.as_view(), name="genre-list"),
    path("genres/create/", views.GenreCreateView.as_view(), name="genre-create"),
    path("genres/<int:pk>/update/", views.GenreUpdateView.as_view(), name="genre-update"),
    path("genres/<int:pk>/delete/", views.GenreDeleteView.as_view(), name="genre-delete"),

    path("borrowings/my/", views.MyBorrowingsListView.as_view(), name="my-borrowings"),
    path("borrowings/<int:pk>/return/", views.ReturnBorrowingView.as_view(), name="borrowing-return"),
]
