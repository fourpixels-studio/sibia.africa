from django.urls import path
from .views import index, about, contact, newsletter_subscription

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("newsletter-subscription/", newsletter_subscription,
         name="newsletter_subscription"),
]
