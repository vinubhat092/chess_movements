from django.db import models
from django.conf import settings
# Create your models here.
User = settings.AUTH_USER_MODEL

class ChessPiece(models.Model):
    user = models.ForeignKey(User,default=1,null=True,on_delete=models.SET_NULL)
    Queen = models.CharField(max_length=10,default=1,null=True)
    Bishop = models.CharField(max_length=10,default=1,null=True)
    Rook = models.CharField(max_length=10,default=1,null=True)
    Knight = models.CharField(max_length=10,default=1,null=True)