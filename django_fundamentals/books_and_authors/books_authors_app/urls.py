from django.urls import path
from .views import *

urlpatterns = [
    path('books', books),
    path('books/create', create_book),
    path('books/<int:id>', one_book),
    path('books/add_author', add_author),
    path('authors', authors),
    path('authors/create', create_author),
    path('authors/<int:id>', one_author),
    path('authors/add_book', add_book),
]