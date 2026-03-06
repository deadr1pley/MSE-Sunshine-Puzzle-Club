from django.urls import path
from .views import puzzle_list, add_puzzle

urlpatterns = [
    path('', puzzle_list, name='puzzle_list'),
    path('add/', add_puzzle, name='add_puzzle'),
]