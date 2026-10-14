from django.db import models

# Create your models here.
class Product(models.Model):
    category= models.ForeignKey('categories.Category', on_delete=models.CASCADE, related_name='Products' )
    name= models.CharField(max_length=255)
    description= models.TextField()
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    specifications = models.TextField(blank=True, null=True)
    price= models.DecimalField(max_digits=10, decimal_places=2)
    created_at= models.TimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name