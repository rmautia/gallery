from django.test import TestCase
from .models import Image, Category,Location

# Create your tests here.

class CategoryTestClass(TestCase):
    # Set up Method
    def setUp(self):
        self.cat = Category(name="fashion")
        self.cat.save_category()
