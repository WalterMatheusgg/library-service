from catalog.models import Author, Book, Genre

fantasy, _ = Genre.objects.get_or_create(name="Fantasy")
programming, _ = Genre.objects.get_or_create(name="Programming")
classic, _ = Genre.objects.get_or_create(name="Classic")

tolkien, _ = Author.objects.get_or_create(
    first_name="J.R.R.",
    last_name="Tolkien",
)

martin, _ = Author.objects.get_or_create(
    first_name="Robert C.",
    last_name="Martin",
)

orwell, _ = Author.objects.get_or_create(
    first_name="George",
    last_name="Orwell",
)

book1, _ = Book.objects.get_or_create(
    title="The Hobbit",
    author=tolkien,
    defaults={
        "inventory": 3,
        "description": "A fantasy adventure about Bilbo Baggins and his unexpected journey.",
        "cover_url": "https://covers.openlibrary.org/b/isbn/9780547928227-L.jpg",
    },
)
book1.genres.set([fantasy])

book2, _ = Book.objects.get_or_create(
    title="Clean Code",
    author=martin,
    defaults={
        "inventory": 2,
        "description": "A practical guide to writing readable, maintainable and professional code.",
        "cover_url": "https://covers.openlibrary.org/b/isbn/9780132350884-L.jpg",
    },
)
book2.genres.set([programming])

book3, _ = Book.objects.get_or_create(
    title="1984",
    author=orwell,
    defaults={
        "inventory": 4,
        "description": "A classic dystopian novel about surveillance, power and social control.",
        "cover_url": "https://covers.openlibrary.org/b/isbn/9780451524935-L.jpg",
    },
)
book3.genres.set([classic])
