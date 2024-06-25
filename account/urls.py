from django.urls import path
from .views import account_signin, account_signout

urlpatterns = [
    path("signin/", account_signin, name="account_signin"),
    path("signout/", account_signout, name="account_signout"),
]
