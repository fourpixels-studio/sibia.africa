from django.contrib import admin
from .models import NewsletterSubscription, Homepage, PrivacyPolicy, TermsOfService, FrequentlyAskedQuestion, Help

admin.site.register(NewsletterSubscription)
admin.site.register(Homepage)
admin.site.register(PrivacyPolicy)
admin.site.register(TermsOfService)
admin.site.register(FrequentlyAskedQuestion)
admin.site.register(Help)
