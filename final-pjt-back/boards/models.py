from django.db import models
from accounts.models import User

# Create your models here.
class Board(models.Model):
  title = models.TextField()
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
  board = models.ForeignKey(Board,on_delete=models.CASCADE)
  content = models.CharField(max_length=250)