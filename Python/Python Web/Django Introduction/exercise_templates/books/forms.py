from django import forms
from .models import Book

class BookFormBase(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'price', 'isbn', 'genre', 'publishing_date', 'description', 'image']

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

        error_messages = {
            'isbn': {'min_length': 'ISBN трябва да е поне 12 символа'},
            }


    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 1:
            raise forms.ValidationError('Цена не може да бъде под 1 лв.')
        return price

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get('title')
        description = cleaned_data.get('description')
        if title == description:
            raise forms.ValidationError('Заглавието не може да бъде еднакво с описанието.')
        return cleaned_data


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

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


