from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    category = models.ManyToManyField('Category', related_name='notes', blank=True)

class Category(models.Model):
    name = models.CharField(max_length=100)
