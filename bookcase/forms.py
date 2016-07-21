from django.forms import ModelForm
from bookcase.models import BookCase

"""
Setiap ModelForm harus memiliki atribut fields atau exclude
"""


class BookCaseForm(ModelForm):
    class Meta:
        # validation rules diambil dari model BookCase
        model = BookCase
        """
        field-field yang di tampilkan
        """
        # fields = [
        #     'name',
        #     'age',
        # ]
        """
        pengecualian, field yang ada di daftar ini tidak akan ditampilkan
        """
        exclude = ['id']
