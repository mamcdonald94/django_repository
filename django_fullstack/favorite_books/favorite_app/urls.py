from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('user/create_user', views.create_user),
    path('user/dashboard', views.dashboard),
    path('user/logout', views.logout),
    path('user/login', views.login),
    path('book/create_book', views.create_book),
    path('book/<int:book_id>/edit', views.edit_book),
    path('book/<int:book_id>/delete', views.delete_book),
    path('book/<int:book_id>', views.book_info),
    path('book/<int:book_id>/remove_favorite', views.remove_favorite),
    path('book/<int:book_id>/add_favorite', views.add_favorite),
]