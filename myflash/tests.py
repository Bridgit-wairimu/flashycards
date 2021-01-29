from django.test import TestCase
from .models import FlashCards

# Create your tests here.
class TestFlashCards(TestCase):
    def setUp(self):
        self.flashcards = FlashCards(id=1,name='Nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.title_test))


     def test_save_method(self):
        self.flashcards.save_flash_cards()
        flashcards=FlashCards.objects.all()
        self.assertTrue(len(flashcards) > 0)  