from django.db import models
from user.models import UserModel

# Create your models here.
class ReviewModel(models.Model):
    class Meta:
        db_table = "review"

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    image = models.ImageField(null=False)
    content = models.CharField(max_length=255,null=True)
    rating = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    size = models.CharField(max_length=255, null=False, default='')
    product_info = models.CharField(max_length=255, null=True)
    purchase_info = models.CharField(max_length=255, null=True)