from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

from django.urls import reverse
from django.db.models.signals import post_save



# Create your models here.
class FlashCards(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length =30)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="flashcards", blank=True,null=True)
    description = models.TextField(max_length =200, blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    category = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='media/', blank=True, null=True, default='default.jpg')
    images = CloudinaryField('images')
    def __str__(self):
        return str(self.name)


    def save_flash_cards(self):
        self.save()

    def delete_flash_cards(self):
        self.delete()


    @classmethod
    def update_flash_cards(cls, id, value):
        cls.objects.filter(id=id).update(name = value)
        
    def get_absolute_url(self):
        return reverse('index')





