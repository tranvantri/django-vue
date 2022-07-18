from django.urls import path, include
from . import views

urlpatterns = [
    path('books/', views.BooksList.as_view()),
    path('book/<int:id>', views.BookDetail.as_view()),
    path('categories/', views.AllCategories.as_view()),
    path('authors/', views.AllCategories.as_view())
]