
import logging
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from collection.models import Collection

logger = logging.getLogger(__name__)

class ISBNForm(forms.Form):
    isbn = forms.CharField(label='ISBN', max_length=20, widget=forms.TextInput(attrs={'placeholder': 'ISBN'}))
    
    def __init__(self, *args, **kwargs):
        super(ISBNForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('isbn', css_class='form-group col-lg-4 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', '検索')
        )

    def clean_isbn(self):
        isbn = self.cleaned_data["isbn"]
        isbn = isbn.replace("-", "")
        logger.info(isbn)
        if len(isbn) == 10 or len(isbn) == 13:
            return isbn
        raise forms.ValidationError("10桁か13桁のiSBNコードを入力してください")


class RegistrationForm(forms.Form):
    title = forms.CharField(label='書名', widget=forms.TextInput(attrs={'placeholder': '書名'}))
    author = forms.CharField(label='著者', widget=forms.TextInput(attrs={'placeholder': '著者'}))
    publisher = forms.CharField(label='発行元', widget=forms.TextInput(attrs={'placeholder': '発行元'}))
    price = forms.CharField(label='価格', required=False,  widget=forms.TextInput(attrs={'placeholder': '価格'}))
    pubdate = forms.CharField(label='発行日', required=False,  widget=forms.TextInput(attrs={'placeholder': '発行日'}))
    text = forms.CharField(label='内容', required=False,  widget=forms.Textarea(attrs={'placeholder': '内容'}))

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-lg-8 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('author', css_class='form-group col-lg-8 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('publisher', css_class='form-group col-lg-6 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('price', css_class='form-group col-lg-2 mb-0'),
                Column('pubdate', css_class='form-group col-lg-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('text', css_class='form-group col-lg-8 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', '登録'),
        )

    def save(self):
        logger.info("")
        collection = Collection(title=self.cleaned_data["title"], author=self.cleaned_data["author"], publisher=self.cleaned_data["publisher"])
        collection.save()


