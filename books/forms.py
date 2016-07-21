from django.forms import ModelForm
from books.models import Books

"""
Setiap ModelForm harus memiliki atribut fields atau exclude
"""


class BookForm(ModelForm):
    class Meta:
        # validation rules diambil dari model Books
        model = Books
        """
        field-field yang di tampilkan
        """
        fields = [
            'book_case',
            'title',
            'authors',
            'sub_topic',
            'publisher',
            'pages',
            'price',
            'tags',
            'year'
        ]
        """
        pengecualian, field yang ada di daftar ini tidak akan ditampilkan
        """
        # exclude = ['fieldname']
