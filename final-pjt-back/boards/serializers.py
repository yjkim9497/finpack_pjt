from rest_framework import serializers
from .models import Board,Comment
from django.contrib.auth import get_user_model

class BoardListSerializer(serializers.ModelSerializer):
  class UserSerializer(serializers.ModelSerializer):
    class Meta:
      model = get_user_model()
      fields = ('username',)
  user = UserSerializer(read_only=True)
  class Meta:
    model = Board
    fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = '__all__'
    read_only_fields = ('board',)

class BoardSerializer(serializers.ModelSerializer):
  class CommentSerializer(serializers.ModelSerializer):
    class Meta:
      model = Comment
      fields = ('content',)
  comment_set = CommentSerializer(many=True, read_only=True)

  class UserSerializer(serializers.ModelSerializer):
    class Meta:
      model = get_user_model()
      fields = ('username',)
  user = UserSerializer(read_only=True)
  class Meta:
    model = Board
    fields = '__all__'
    read_only_fields = ('user',)

class CommentListSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = ('id','content',)


