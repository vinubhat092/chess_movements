from rest_framework import serializers
from .models import ChessPiece
class ChessMoveSerializer(serializers.Serializer):
    Queen = serializers.CharField()
    Bishop = serializers.CharField()
    Rook = serializers.CharField()
    Knight = serializers.CharField()

    class Meta:
        model = ChessPiece
    
        fields = [
            'Queen',
            'Bishop',
            'Rook',
            'Knight'


        ]