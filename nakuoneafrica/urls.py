from django.urls import path
from .views import nakuoneafrica, article_detail, article_list

urlpatterns = [
    path("", nakuoneafrica, name="nakuoneafrica"),
    path("articles/", article_list, name="article_list"),
    path("article/<slug:slug>/", article_detail, name="article_detail"),
]
