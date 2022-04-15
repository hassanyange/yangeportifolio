from django.db import models

# Create your models here.
class Cards(models.Model):
    imageupload = models.ImageField(upload_to = 'media')
    Title_of_card = models.CharField(max_length= 30)
    link_of_the_card =models.TextField(max_length= 100)
    commment = models.CharField(max_length=500)
    
    def __str__(self):
        return self.Title_of_the_card 