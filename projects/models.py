from django.db import models

# Create your models here.
class Cards(models.Model):
    imageupload = models.ImageField(upload_to = 'media')
    Title_of_card = models.CharField(max_length= 30)
    heroku_link = models.CharField(max_length=30)
    github_link = models.CharField(max_length=30)
    commment = models.CharField(max_length=100)
    
    def __str__(self):
        return self.Title_of_the_card 