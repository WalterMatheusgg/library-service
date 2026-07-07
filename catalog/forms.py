from django import forms

from catalog.models import Author, Book, Borrowing, Genre


class BootstrapFormMixin:
    def apply_bootstrap_classes(self):
        for field in self.fields.values():
            widget = field.widget

            if isinstance(widget, forms.Select):
                widget.attrs.update({"class": "form-select"})
            elif isinstance(widget, forms.CheckboxSelectMultiple):
                widget.attrs.update({"class": "form-check-input"})
            else:
                widget.attrs.update({"class": "form-control"})


class AuthorForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Author
        fields = ["first_name", "last_name", "date_of_birth"]
        widgets = {
            "date_of_birth": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_bootstrap_classes()


class GenreForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Genre
        fields = ["name"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_bootstrap_classes()


class BookForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "genres",
            "inventory",
            "description",
            "cover_url",
        ]
        widgets = {
            "genres": forms.CheckboxSelectMultiple,
            "description": forms.Textarea(attrs={"rows": 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_bootstrap_classes()


class BorrowingForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Borrowing
        fields = ["due_date"]
        widgets = {
            "due_date": forms.DateInput(attrs={"type": "date"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_bootstrap_classes()
