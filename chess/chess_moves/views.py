from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import get_valid_moves_queen, get_valid_moves_bishop, get_valid_moves_rook, get_valid_moves_knight
from .serializers import ChessMoveSerializer
import json

@api_view(['POST','GET'])
def get_valid_moves(request,slug):
    print("dsd",slug)
    serializer = ChessMoveSerializer(data=request.data)
    

    if serializer.is_valid():
        data = serializer.validated_data
        print("dataaa",data)
        valid_moves = []
        specific_list = []
        a = get_valid_moves_queen(data['Queen'])
        b = get_valid_moves_bishop(data['Bishop'])
        c = get_valid_moves_rook(data['Rook'])
        d = get_valid_moves_knight(data['Knight'])
        if data.get('Queen'):
            if slug != "queen":
                valid_moves.extend(get_valid_moves_queen(data['Queen']))

        if data.get('Bishop'):
            if slug != "bishop":
                valid_moves.extend(get_valid_moves_bishop(data['Bishop']))

        if data.get('Rook'):
            if slug != "rook":
                valid_moves.extend(get_valid_moves_rook(data['Rook']))

        if data.get('Knight'):
            if slug != "knight":
                valid_moves.extend(get_valid_moves_knight(data['Knight']))

        # if data.get(slug):
        print("sdsd")
        if slug == "queen":
            print("comingggg")
            print("asd",valid_moves)
            print("asdfd",a)
            for item in a:
                if item not in valid_moves:
                    specific_list.append(item)

        if slug == "bishop":
            print("comingggg")
            print("asd",valid_moves)
            print("asdfd",b)
            for item in b:
                if item not in valid_moves:
                    specific_list.append(item)

        if slug == "rook":
            print("comingggg")
            print("asd",valid_moves)
            print("asdfd",c)
            for item in c:
                if item not in valid_moves:
                    specific_list.append(item)

        if slug == "knight":
            print("comingggg")
            print("asd",valid_moves)
            print("asdfd",d)
            for item in d:
                if item not in valid_moves:
                    specific_list.append(item)
   

        return Response({"valid_moves": specific_list})
    else:
        return Response(serializer.errors, status=400)
    
# @api_view(['POST'])
# def get_valid_moves_queen(request):
#     serializer = ChessMoveSerializer(data=request.data)

#     if serializer.is_valid():
#         data = serializer.validated_data
#         print("dataaa",data)
#         valid_moves = []

#         if data.get('Queen'):
#             valid_moves.extend(get_valid_moves_queen(data['Queen']))

#         # if data.get('Bishop'):
#         #     valid_moves.extend(get_valid_moves_bishop(data['Bishop']))

#         # if data.get('Rook'):
#         #     valid_moves.extend(get_valid_moves_rook(data['Rook']))

#         # if data.get('Knight'):
#         #     valid_moves.extend(get_valid_moves_knight(data['Knight']))

#         return Response({"valid_moves": valid_moves})
#     else:
#         return Response(serializer.errors, status=400)
    