from django.conf import settings
from django.db import models
from django.urls import reverse


class Author(models.Model):
    first_name = models.CharField("nome", max_length=100)
    last_name = models.CharField("sobrenome", max_length=100)
    date_of_birth = models.DateField(
        "data de nascimento",
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name = "Autor"
        verbose_name_plural = "Autores"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("catalog:author-detail", kwargs={"pk": self.pk})


class Genre(models.Model):
    name = models.CharField("nome", max_length=100, unique=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Gênero"
        verbose_name_plural = "Gêneros"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("catalog:genre-list")


class Book(models.Model):
    title = models.CharField("título", max_length=200)
    author = models.ForeignKey(
        Author,
        verbose_name="autor",
        on_delete=models.CASCADE,
        related_name="books",
    )
    genres = models.ManyToManyField(
        Genre,
        verbose_name="gêneros",
        related_name="books",
        blank=True,
    )
    inventory = models.PositiveIntegerField(
        "quantidade no acervo",
        default=1,
    )
    description = models.TextField("descrição", blank=True)
    cover_url = models.URLField("URL da capa", blank=True)

    class Meta:
        ordering = ["title"]
        verbose_name = "Livro"
        verbose_name_plural = "Livros"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("catalog:book-detail", kwargs={"pk": self.pk})

    @property
    def active_borrowings_count(self):
        return self.borrowings.filter(returned_at__isnull=True).count()

    @property
    def available_copies(self):
        available = self.inventory - self.active_borrowings_count
        return max(available, 0)


class Borrowing(models.Model):
    book = models.ForeignKey(
        Book,
        verbose_name="livro",
        on_delete=models.CASCADE,
        related_name="borrowings",
    )
    borrower = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="usuário",
        on_delete=models.CASCADE,
        related_name="borrowings",
    )
    borrowed_at = models.DateTimeField("data do empréstimo", auto_now_add=True)
    due_date = models.DateField("data de devolução")
    returned_at = models.DateTimeField(
        "data em que foi devolvido",
        null=True,
        blank=True,
    )

    class Meta:
        ordering = ["-borrowed_at"]
        verbose_name = "Empréstimo"
        verbose_name_plural = "Empréstimos"

    def __str__(self):
        return f"{self.book.title} emprestado para {self.borrower.username}"

    @property
    def is_active(self):
        return self.returned_at is None
