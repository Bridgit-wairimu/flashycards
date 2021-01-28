from django.db import models
import datetime as dt
from cloudinary.models import CloudinaryField

# Create your models here.
class FlashCards(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length =30)
    description = models.TextField(max_length =200, blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    category = models.CharField(max_length=200, blank=True, null=True)
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



