from django.urls import path
from .views import index, about, contact, newsletter_subscription, help, request_appointment
from .crud_methods import edit_homepage

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("contact/", contact, name="contact"),
    path("request-appointment/", request_appointment, name="request_appointment"),
    path("edit/homepage/<int:pk>/", edit_homepage, name="edit_homepage"),
    path("help/", help, name="help"),
    path("newsletter-subscription/", newsletter_subscription, name="newsletter_subscription"),
]
