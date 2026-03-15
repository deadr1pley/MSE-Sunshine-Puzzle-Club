from django.urls import path
from .views import puzzle_list, add_puzzle, edit_puzzle, delete_puzzle

urlpatterns = [
    path('', puzzle_list, name='puzzle_list'),
    path('add/', add_puzzle, name='add_puzzle'),
    path('add/', add_puzzle, name='add_puzzle'),
    path('edit/<int:puzzle_id>/', edit_puzzle, name='edit_puzzle'),
    path('delete/<int:puzzle_id>/', delete_puzzle, name='delete_puzzle'),
]