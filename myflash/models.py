from django.db import models



# Create your models here.

class FlashCards(models.Model):
    name = models.CharField(max_length =30)
    
    def __str__(self):
        return str(self.name)

    def save_flash_cards(self):
        self.save()

    def delete_flash_cards(self):
        self.delete()


    @classmethod
    def update_flash_cards(cls, id, value):
        cls.objects.filter(id=id).update(name = value)



    
    


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return str(self.name)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()


    @classmethod
    def update_category(cls, id, value):
        cls.objects.filter(id=id).update(name = value)