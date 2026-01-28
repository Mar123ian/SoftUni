from django import forms
from .models import Book

class BookFormBase(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'price', 'isbn', 'genre', 'publishing_date', 'description', 'image_url']

        labels = {
            'title': 'Заглавие',
            'price': 'Цена',
            'isbn': 'ISBN',
            'genre': 'Жанр',
            'publishing_date': 'Дата на издаване',
            'description': 'Описание',
            'image_url': 'Изображение',
        }

        widgets = {
            'genre': forms.Select(choices=Book.Genre.choices),
            'publishing_date': forms.DateInput(attrs={'type':"date"}),
        }



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['image_url'].initial = 'https://'
        self.fields['description'].required = False




class AddBookForm(BookFormBase):
    pass

class UpdateBookForm(BookFormBase):
    pass

class DeleteBookForm(BookFormBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs['disabled'] = True
            self.fields[field].required = False


