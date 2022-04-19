
from django.db import models

# Create your models here.
class Cards(models.Model):
    imageupload = models.ImageField(upload_to = 'media')
    Title_of_card = models.CharField(max_length= 30)
    heroku_link = models.CharField(max_length=30 , default= 'https://dashboard.heroku.com/apps/yange-portifolio-project')
    github_link = models.CharField(max_length=30, default= 'https://github.com/hassanyange/yangeshop.git')
    commment = models.CharField(max_length=100 , default= 'small explanations')
    
    
    def __str__(self):
        return self.Title_of_card 
    
class Form(models.Model) :
    FirstName = models.CharField(max_length=25)
    LastName = models.CharField(max_length=25)
    Email = models.EmailField(max_length=100)
    Message = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.Name    