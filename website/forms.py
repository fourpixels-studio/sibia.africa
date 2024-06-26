from django import forms
from .models import NewsletterSubscription, Homepage, Appointment


class NewsletterSubscriptionForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ['email']


class HomepageForm(forms.ModelForm):
    class Meta:
        model = Homepage
        fields = ('__all__')


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            'name',
            'email',
            'phone',
            'message',
        ]
