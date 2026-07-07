from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from catalog.models import Author, Book, Genre


class Command(BaseCommand):
    help = "Cria dados de exemplo para o projeto Biblioteca Digital."

    def handle(self, *args, **options):
        User = get_user_model()

        demo_user, created_user = User.objects.get_or_create(
            username="demo",
            defaults={
                "email": "demo@example.com",
            },
        )

        if created_user:
            demo_user.set_password("demo12345")
            demo_user.save()

        genres = {}

        genre_names = [
            "Romance",
            "Clássico",
            "Literatura brasileira",
            "Ficção distópica",
            "Fantasia",
            "Programação",
            "Filosofia",
            "Realismo",
            "Modernismo",
            "Aventura",
        ]

        for name in genre_names:
            genres[name], _ = Genre.objects.get_or_create(name=name)

        authors_data = [
            {
                "key": "machado",
                "first_name": "Machado",
                "last_name": "de Assis",
                "date_of_birth": "1839-06-21",
            },
            {
                "key": "aluisio",
                "first_name": "Aluísio",
                "last_name": "Azevedo",
                "date_of_birth": "1857-04-14",
            },
            {
                "key": "clarice",
                "first_name": "Clarice",
                "last_name": "Lispector",
                "date_of_birth": "1920-12-10",
            },
            {
                "key": "jorge",
                "first_name": "Jorge",
                "last_name": "Amado",
                "date_of_birth": "1912-08-10",
            },
            {
                "key": "guimaraes",
                "first_name": "João Guimarães",
                "last_name": "Rosa",
                "date_of_birth": "1908-06-27",
            },
            {
                "key": "orwell",
                "first_name": "George",
                "last_name": "Orwell",
                "date_of_birth": "1903-06-25",
            },
            {
                "key": "saint_exupery",
                "first_name": "Antoine",
                "last_name": "de Saint-Exupéry",
                "date_of_birth": "1900-06-29",
            },
            {
                "key": "tolkien",
                "first_name": "J.R.R.",
                "last_name": "Tolkien",
                "date_of_birth": "1892-01-03",
            },
            {
                "key": "martin",
                "first_name": "Robert C.",
                "last_name": "Martin",
                "date_of_birth": "1952-12-05",
            },
            {
                "key": "rowling",
                "first_name": "J.K.",
                "last_name": "Rowling",
                "date_of_birth": "1965-07-31",
            },
            {
                "key": "austen",
                "first_name": "Jane",
                "last_name": "Austen",
                "date_of_birth": "1775-12-16",
            },
            {
                "key": "nietzsche",
                "first_name": "Friedrich",
                "last_name": "Nietzsche",
                "date_of_birth": "1844-10-15",
            },
        ]

        authors = {}

        for author_data in authors_data:
            key = author_data.pop("key")

            author, _ = Author.objects.get_or_create(
                first_name=author_data["first_name"],
                last_name=author_data["last_name"],
                defaults={
                    "date_of_birth": author_data["date_of_birth"],
                },
            )

            authors[key] = author

        books_data = [
            {
                "title": "Dom Casmurro",
                "author": authors["machado"],
                "inventory": 5,
                "description": (
                    "Um dos romances mais importantes da literatura brasileira, "
                    "marcado pela ambiguidade narrativa e pela complexidade psicológica "
                    "de Bentinho e Capitu."
                ),
                "cover_url": "https://covers.openlibrary.org/b/title/Dom%20Casmurro-L.jpg",
                "genres": ["Romance", "Clássico", "Literatura brasileira", "Realismo"],
            },
            {
                "title": "Memórias Póstumas de Brás Cubas",
                "author": authors["machado"],
                "inventory": 4,
                "description": (
                    "Obra fundamental do Realismo brasileiro, narrada por um defunto autor "
                    "que observa a sociedade com ironia e crítica refinada."
                ),
                "cover_url": "https://covers.openlibrary.org/b/title/Memorias%20Postumas%20de%20Bras%20Cubas-L.jpg",
                "genres": ["Romance", "Clássico", "Literatura brasileira", "Realismo"],
            },
            {
                "title": "O Cortiço",
                "author": authors["aluisio"],
                "inventory": 4,
                "description": (
                    "Romance naturalista que retrata a vida coletiva em um cortiço carioca, "
                    "abordando desigualdade social, ambição e transformação urbana."
                ),
                "cover_url": "https://covers.openlibrary.org/b/title/O%20Cortico-L.jpg",
                "genres": ["Romance", "Clássico", "Literatura brasileira"],
            },
            {
                "title": "A Hora da Estrela",
                "author": authors["clarice"],
                "inventory": 3,
                "description": (
                    "Romance modernista centrado em Macabéa, personagem marcada pela "
                    "simplicidade, solidão e invisibilidade social."
                ),
                "cover_url": "https://covers.openlibrary.org/b/title/A%20Hora%20da%20Estrela-L.jpg",
                "genres": ["Romance", "Literatura brasileira", "Modernismo"],
            },
            {
                "title": "Capitães da Areia",
                "author": authors["jorge"],
                "inventory": 4,
                "description": (
                    "Romance social sobre um grupo de meninos em situação de rua em Salvador, "
                    "abordando infância, exclusão e resistência."
                ),
                "cover_url": "https://covers.openlibrary.org/b/title/Capitaes%20da%20Areia-L.jpg",
                "genres": ["Romance", "Literatura brasileira"],
            },
            {
                "title": "Grande Sertão: Veredas",
                "author": authors["guimaraes"],
                "inventory": 2,
                "description": (
                    "Obra-prima da literatura brasileira, marcada por linguagem inovadora, "
                    "reflexões filosóficas e narrativa ambientada no sertão."
                ),
                "cover_url": "https://covers.openlibrary.org/b/title/Grande%20Sertao%20Veredas-L.jpg",
                "genres": ["Romance", "Clássico", "Literatura brasileira", "Modernismo"],
            },
            {
                "title": "1984",
                "author": authors["orwell"],
                "inventory": 5,
                "description": (
                    "Romance distópico sobre vigilância, controle político, manipulação "
                    "da verdade e perda da liberdade individual."
                ),
                "cover_url": "https://covers.openlibrary.org/b/isbn/9780451524935-L.jpg",
                "genres": ["Ficção distópica", "Clássico"],
            },
            {
                "title": "O Pequeno Príncipe",
                "author": authors["saint_exupery"],
                "inventory": 6,
                "description": (
                    "Narrativa poética e filosófica sobre amizade, imaginação, infância "
                    "e a forma como os adultos enxergam o mundo."
                ),
                "cover_url": "https://covers.openlibrary.org/b/title/O%20Pequeno%20Principe-L.jpg",
                "genres": ["Clássico", "Filosofia"],
            },
            {
                "title": "O Hobbit",
                "author": authors["tolkien"],
                "inventory": 4,
                "description": (
                    "Aventura de fantasia que acompanha Bilbo Bolseiro em uma jornada "
                    "inesperada pela Terra Média."
                ),
                "cover_url": "https://covers.openlibrary.org/b/isbn/9780547928227-L.jpg",
                "genres": ["Fantasia", "Aventura", "Clássico"],
            },
            {
                "title": "Clean Code",
                "author": authors["martin"],
                "inventory": 3,
                "description": (
                    "Livro técnico sobre boas práticas de programação, legibilidade, "
                    "manutenção e qualidade de código."
                ),
                "cover_url": "https://covers.openlibrary.org/b/isbn/9780132350884-L.jpg",
                "genres": ["Programação"],
            },
            {
                "title": "Harry Potter e a Pedra Filosofal",
                "author": authors["rowling"],
                "inventory": 5,
                "description": (
                    "Primeiro livro da série Harry Potter, apresentando Hogwarts, magia, "
                    "amizade e a jornada inicial do jovem bruxo."
                ),
                "cover_url": "https://covers.openlibrary.org/b/title/Harry%20Potter%20e%20a%20Pedra%20Filosofal-L.jpg",
                "genres": ["Fantasia", "Aventura"],
            },
            {
                "title": "Orgulho e Preconceito",
                "author": authors["austen"],
                "inventory": 4,
                "description": (
                    "Clássico romance inglês que aborda relações sociais, casamento, "
                    "orgulho, julgamento e amadurecimento afetivo."
                ),
                "cover_url": "https://covers.openlibrary.org/b/title/Orgulho%20e%20Preconceito-L.jpg",
                "genres": ["Romance", "Clássico"],
            },
            {
                "title": "Assim Falou Zaratustra",
                "author": authors["nietzsche"],
                "inventory": 2,
                "description": (
                    "Obra filosófica escrita em estilo poético, explorando temas como "
                    "superação, valores, moralidade e existência."
                ),
                "cover_url": "https://covers.openlibrary.org/b/title/Assim%20Falou%20Zaratustra-L.jpg",
                "genres": ["Filosofia", "Clássico"],
            },
        ]

        for book_data in books_data:
            genre_names = book_data.pop("genres")

            book, _ = Book.objects.get_or_create(
                title=book_data["title"],
                author=book_data["author"],
                defaults={
                    "inventory": book_data["inventory"],
                    "description": book_data["description"],
                    "cover_url": book_data["cover_url"],
                },
            )

            book.genres.set([genres[name] for name in genre_names])

        self.stdout.write(
            self.style.SUCCESS("Dados de exemplo criados com sucesso.")
        )
        self.stdout.write(
            self.style.SUCCESS("Foram cadastrados autores, gêneros e livros reais.")
        )
        self.stdout.write(
            self.style.SUCCESS("Usuário de teste: demo | Senha: demo12345")
        )
