from django.contrib import admin
from django.urls import path
from tema_28 import views as views_28
from tema_29 import views as views_29

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tema-28/', views_28.exercitiu),
    path('tema-29/', views_29.exercitiu),
]
