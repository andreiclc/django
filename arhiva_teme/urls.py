from django.contrib import admin
from django.urls import path
from tema_29 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.exercitiu),
]
