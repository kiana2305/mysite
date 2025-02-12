from django.db import models

# Create your models here.

class Post(models.Model):
    # image_url = models.URLField(null=True, blank=True)
    # author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    # tag = models.CharField(max_length=255)
    # category = models.ForeignKey('Category', on_delete=models.CASCADE)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    published_date = models.DateTimeField(null=True) 
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    
    
    
