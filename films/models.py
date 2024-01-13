from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    class Meta: 
        app_label = 'films'


class Film(models.Model):
    title = models.CharField(max_length = 100)
    tags = models.ManyToManyField(Tag)
    ordinal_number = models.IntegerField()
    
    def __str__ (self):
        return self.title
    
class Article(models.Model):
    title = models.CharField(max_length = 200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.title