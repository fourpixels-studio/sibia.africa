from django import forms
from .models import Article
from django_summernote.widgets import SummernoteWidget


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = [
            "title",
            "content",
            "summary",
            "category",
            "cover_image",
            "meta_thumbnail"
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title of article'}),
            'summary': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Summary of article'}),
            'content': SummernoteWidget(attrs={'class': 'form-control'}),
            'cover_image': forms.ClearableFileInput(attrs={'class': 'form-control text-brown'}),
            'meta_thumbnail': forms.ClearableFileInput(attrs={'class': 'form-control text-brown'}),
        }
