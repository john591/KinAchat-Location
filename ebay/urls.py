from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sous_categorie_view/<int:sous_cate_id>/", views.sous_categorie_view, name="sous_categorie_view"),
    path("articles_view/<int:article_id>/", views.articles_view, name="articles_view"),
    path("achat_article/<int:item_id>/", views.achat_article, name="achat_article"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("apropos/", views.apropos_view, name="apropos")
]
