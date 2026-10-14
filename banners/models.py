from django.db import models

# Create your models here.
class Banner(models.Model):
    image= models.ImageField(upload_to='banners/')
    title= models.CharField(max_length=30)
    content= models.TextField(blank=True)
    link= models.URLField(max_length=500, blank= True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title