from django import forms

class BookForm(forms.Form):
    book_title = forms.CharField(max_length=100)
