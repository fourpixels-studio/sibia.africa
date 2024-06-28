from django.urls import path
from .views import nakuoneafrica, article_detail, article_list, articles_listed_by_sdg
from .crud_methods import edit_article, new_article, new_sdg, edit_sdg

urlpatterns = [
    path("", nakuoneafrica, name="nakuoneafrica"),
    path("articles/", article_list, name="article_list"),
    path("articles/SDGs/<slug:slug>/", articles_listed_by_sdg,
         name="articles_listed_by_sdg"),
    path("article/<slug:slug>/", article_detail, name="article_detail"),
    path("editing/article/<int:pk>/", edit_article, name="edit_article"),
    path("new-article/", new_article, name="new_article"),
    path("new-SDG/", new_sdg, name="new_sdg"),
    path("edit-SDG/<int:pk>/", edit_sdg, name="edit_sdg"),
]
