from django import forms
from .models import NewsletterSubscription, Homepage, FrequentlyAskedQuestion


class NewsletterSubscriptionForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ['email']


class HomepageForm(forms.ModelForm):
    class Meta:
        model = Homepage
        fields = ('__all__')


class FrequentlyAskedQuestionForm(forms.ModelForm):
    class Meta:
        model = FrequentlyAskedQuestion
        fields = ('__all__')
