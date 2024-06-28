from django import forms
from .models import Article, SDG
from django_summernote.widgets import SummernoteWidget


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = [
            "title",
            "content",
            "summary",
            "sdg",
            "cover_image",
            "attachment",
            "meta_thumbnail",
            "is_published",
        ]
        widgets = {
            'title': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Title of article',
                'style': 'height: 70px;',
            }),
            'summary': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Summary of article',
                'style': 'height: 100px;',
            }),
            'content': SummernoteWidget(attrs={'class': 'form-control'}),
            'cover_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'attachment': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'meta_thumbnail': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'is_published': forms.CheckboxInput(attrs={'class': 'form-check-input hover'}),
            'sdg': forms.Select(attrs={'class': 'form-control'}),
        }


class SDGForm(forms.ModelForm):

    class Meta:
        model = SDG
        fields = [
            "name",
            "description",
            "icon",
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'New SDG', }),
            'icon': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'SDG Icon', }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Description of SDG',
                'style': 'height: 200px;',
            }),
        }


class EditSDGForm(forms.ModelForm):

    class Meta:
        model = SDG
        fields = [
            "name",
            "description",
            "icon",
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 200px;', }),
            'icon': forms.TextInput(attrs={'class': 'form-control'}),
        }
