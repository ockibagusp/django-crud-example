from django.forms import ModelForm
from authors.models import Author

"""
Setiap ModelForm harus memiliki atribut fields atau exclude
"""


class AuthorForm(ModelForm):
    class Meta:
        # validation rules diambil dari model Author
        model = Author
        """
        field-field yang di tampilkan
        """
        fields = [
            'name',
            'age',
        ]
        """
        pengecualian, field yang ada di daftar ini tidak akan ditampilkan
        """
        # exclude = ['fieldname']
