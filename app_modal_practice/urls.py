from django.urls import path
from . import views

app_name = 'app_modal_practice'

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/create/', views.book_create, name ='book_create'),
    path('books/<int:pk>/update/', views.book_update, name='book_update'),
  
]
