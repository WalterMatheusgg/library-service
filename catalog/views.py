from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import View, generic

from catalog.forms import AuthorForm, BookForm, BorrowingForm, GenreForm
from catalog.models import Author, Book, Borrowing, Genre


class IndexView(generic.TemplateView):
    template_name = "catalog/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        num_visits = self.request.session.get("num_visits", 0) + 1
        self.request.session["num_visits"] = num_visits

        context["num_books"] = Book.objects.count()
        context["num_authors"] = Author.objects.count()
        context["num_genres"] = Genre.objects.count()
        context["num_active_borrowings"] = Borrowing.objects.filter(
            returned_at__isnull=True
        ).count()
        context["num_visits"] = num_visits

        return context


class BookListView(generic.ListView):
    model = Book
    template_name = "catalog/book_list.html"
    context_object_name = "book_list"
    paginate_by = 6

    def get_queryset(self):
        queryset = (
            Book.objects
            .select_related("author")
            .prefetch_related("genres")
        )

        query = self.request.GET.get("q")

        if query:
            queryset = queryset.filter(
                Q(title__icontains=query)
                | Q(author__first_name__icontains=query)
                | Q(author__last_name__icontains=query)
                | Q(genres__name__icontains=query)
            ).distinct()

        return queryset


class BookDetailView(generic.DetailView):
    model = Book
    template_name = "catalog/book_detail.html"
    context_object_name = "book"

    def get_queryset(self):
        return (
            Book.objects
            .select_related("author")
            .prefetch_related("genres", "borrowings")
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["borrowing_form"] = BorrowingForm()
        context["active_borrowings"] = self.object.borrowings.filter(
            returned_at__isnull=True
        ).select_related("borrower")
        return context


class BookCreateView(LoginRequiredMixin, generic.CreateView):
    model = Book
    form_class = BookForm
    template_name = "catalog/book_form.html"


class BookUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Book
    form_class = BookForm
    template_name = "catalog/book_form.html"


class BookDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Book
    template_name = "catalog/book_confirm_delete.html"
    success_url = reverse_lazy("catalog:book-list")


class AuthorListView(generic.ListView):
    model = Author
    template_name = "catalog/author_list.html"
    context_object_name = "author_list"
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = "catalog/author_detail.html"
    context_object_name = "author"


class AuthorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Author
    form_class = AuthorForm
    template_name = "catalog/author_form.html"


class AuthorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = "catalog/author_form.html"


class AuthorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Author
    template_name = "catalog/author_confirm_delete.html"
    success_url = reverse_lazy("catalog:author-list")


class GenreListView(generic.ListView):
    model = Genre
    template_name = "catalog/genre_list.html"
    context_object_name = "genre_list"
    paginate_by = 10


class GenreCreateView(LoginRequiredMixin, generic.CreateView):
    model = Genre
    form_class = GenreForm
    template_name = "catalog/genre_form.html"


class GenreUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Genre
    form_class = GenreForm
    template_name = "catalog/genre_form.html"


class GenreDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Genre
    template_name = "catalog/genre_confirm_delete.html"
    success_url = reverse_lazy("catalog:genre-list")


class MyBorrowingsListView(LoginRequiredMixin, generic.ListView):
    model = Borrowing
    template_name = "catalog/my_borrowings.html"
    context_object_name = "borrowing_list"

    def get_queryset(self):
        return (
            Borrowing.objects
            .filter(borrower=self.request.user)
            .select_related("book", "book__author")
        )


class BorrowBookView(LoginRequiredMixin, View):
    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)

        if book.available_copies <= 0:
            messages.error(request, "There are no available copies of this book.")
            return redirect(book.get_absolute_url())

        form = BorrowingForm(request.POST)

        if form.is_valid():
            borrowing = form.save(commit=False)
            borrowing.book = book
            borrowing.borrower = request.user
            borrowing.save()

            messages.success(request, "Book borrowed successfully.")
        else:
            messages.error(request, "Please provide a valid due date.")

        return redirect(book.get_absolute_url())


class ReturnBorrowingView(LoginRequiredMixin, View):
    def post(self, request, pk):
        borrowing = get_object_or_404(
            Borrowing,
            pk=pk,
            borrower=request.user,
            returned_at__isnull=True,
        )
        borrowing.returned_at = timezone.now()
        borrowing.save(update_fields=["returned_at"])

        messages.success(request, "Book returned successfully.")

        return redirect("catalog:my-borrowings")
