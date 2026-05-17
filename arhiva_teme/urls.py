from django.contrib import admin
from django.urls import path
from tema_28 import views as views_28
from tema_29 import views as views_29
from tema_30 import views as views_30
from tema_31 import views as views_31

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tema-28/', views_28.exercitiu),
    path('tema-29/', views_29.exercitiu),
    path('tema-30/', views_30.books, name='books'),
    path('tema-30/add/', views_30.add_books, name='add_books'),
    path('tema-30/delete/', views_30.delete_books, name='delete_books'),
    path('tema-30/edit/<uuid:pk>/', views_30.edit_book, name='edit_book'),
    path('tema-31/', views_31.movies, name='movies'),
    path('tema-31/add/', views_31.add_movies, name='add_movies'),
]
