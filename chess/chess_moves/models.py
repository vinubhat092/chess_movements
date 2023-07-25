from django.db import models
from django.conf import settings
# Create your models here.
User = settings.AUTH_USER_MODEL

class ChessPiece(models.Model):
    # user = models.ForeignKey(User,default=1,null=True,on_delete=models.SET_NULL)
    Queen = models.CharField(max_length=10)
    Bishop = models.CharField(max_length=10)
    Rook = models.CharField(max_length=10)
    Knight = models.CharField(max_length=10)