from django.db import models
from accounts.models import User

class Product(models.Model) :
    account = models.ForeignKey(
        User,on_delete=models.CASCADE,related_name='products'
        )
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="image/",blank=True)
    content = models.TextField()
    price = models.PositiveIntegerField()
    

    def __str__(self) :
        return self.title    
