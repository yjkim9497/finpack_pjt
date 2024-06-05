from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404, get_list_or_404

from .serializers import BoardListSerializer, BoardSerializer, CommentSerializer, CommentListSerializer
from .models import Board, Comment


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def board_list(request):
    if request.method == 'GET':
        boards = get_list_or_404(Board)
        serializer = BoardListSerializer(boards, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BoardSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # serializer.save()
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT'])
def board_detail(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)

    if request.method == 'GET':
        serializer = BoardSerializer(board)
        print(serializer.data)
        return Response(serializer.data)
    elif request.method =='PUT':
        serializer = BoardSerializer(instance=board,data=request.data,partial=True)
        print(serializer)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

@api_view(['DELETE'])
def board_delete(request,board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if request.method == 'DELETE':
        board.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def comment_list(request,board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if request.method == 'GET':
        comments = Comment.objects.filter(board=board)
        serializer = CommentListSerializer(comments,many=True)
        return Response(serializer.data)

@api_view(['POST'])
def comments_create(request,board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if request.method == 'POST':
        serailizer = CommentSerializer(data=request.data)
        if serailizer.is_valid(raise_exception=True):
            serailizer.save(board=board)
            return Response(serailizer.data, status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
def comment_delete(request,board_pk,comment_pk):
    comment = get_object_or_404(Comment,pk=comment_pk)
    if request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
