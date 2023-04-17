from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserModel(AbstractUser):
    class Meta:
        db_table = "it_user"

   
    nickname = models.CharField(max_length=20, null=False)
    gender = models.CharField(max_length=20, null=False)
    phone = models.IntegerField(null=False)
    birth_day = models.IntegerField(null=False)

