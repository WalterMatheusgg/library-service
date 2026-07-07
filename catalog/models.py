from django.conf import settings
from django.db import models
from django.urls import reverse


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("catalog:author-detail", kwargs={"pk": self.pk})


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("catalog:genre-list")


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books"
    )
    genres = models.ManyToManyField(
        Genre,
        related_name="books",
        blank=True
    )
    inventory = models.PositiveIntegerField(default=1)
    description = models.TextField(blank=True)
    cover_url = models.URLField(blank=True)

    class Meta:
        ordering = ["title"]

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
        on_delete=models.CASCADE,
        related_name="borrowings"
    )
    borrower = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="borrowings"
    )
    borrowed_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    returned_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ["-borrowed_at"]

    def __str__(self):
        return f"{self.book.title} borrowed by {self.borrower.username}"

    @property
    def is_active(self):
        return self.returned_at is None
