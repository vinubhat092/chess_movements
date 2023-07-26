from django.urls import path
from .views import get_valid_moves,get_valid_moves_queen

urlpatterns = [
    # path('chess/<slug>/', get_valid_moves, name='get_valid_moves'),
    # path('chess/queen/', get_valid_moves, name='get_valid_moves'),
    # path('chess/rook/', get_valid_moves_for_rook, name='get_valid_moves'),
    path('chess/<str:slug>/', get_valid_moves, name='get_valid_moves'),
    # path('api/get_valid_moves/queen/', get_valid_moves, name='get_valid_moves'),
    # path('api/get_valid_moves/', get_valid_moves, name='get_valid_moves'),
    # path('api/get_valid_moves/', get_valid_moves, name='get_valid_moves'),
    # path('chess/bishop/', get_valid_moves, name='get_valid_moves'),
    # path('chess/knight/', get_valid_moves, name='get_valid_moves'),
]