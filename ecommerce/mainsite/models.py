from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class addProduct(models.Model):
    cat_list=(('Dresses','Dresses'),('Blouses','Blouses'),('T-shirts','T-shirts'),('OutWare','OutWare'),('Bags','Bags'),('Other','Other'))
    Title = models.CharField(max_length=200)
    Category = models.CharField(choices=cat_list,max_length=50,default='Other')
    Price = models.IntegerField()
    Discount_Price = models.IntegerField(blank=True,null=True)
    Details = models.TextField()
    Information = models.TextField()
    img = models.ImageField(upload_to='media',default='media/default.BMP')
