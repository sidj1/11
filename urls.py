from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_movies, name='movie_search'),
    path('<slug:slug>/', views.movie_detail, name='movie_detail'),
]
