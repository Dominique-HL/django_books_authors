from django.urls import path
from . import views

urlpatterns = [
    path('',views.books), #página principal
    path('add_book',views.add_book), # Muestra la lista de libros y añade libro
    path('books/<int:book_id>',views.book_info),# Muestra la pagina para un libro
    path('add_authors/<int:book_id>',views.add_authors),
    path('authors',views.authors),
    path('add_author_to_authors',views.add_author_to_authors),
    path('authors/<int:author_id>',views.author_info),
    path('add_books/<int:author_id>',views.add_books)
] 