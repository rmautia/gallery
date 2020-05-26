from django.test import TestCase
from .models import Image, Category,Location

# Create your tests here.

class CategoryTestClass(TestCase):
    # Set up Method
    def setUp(self):
        self.cat = Category(name="food")
        self.cat.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.cat, Category))

    def test_save_method(self):
        self.cat.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

    def test_delete_method(self):
        self.cat.save_category()
        self.cat.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)

    def test_update(self):
        category = Category.get_category_id(self.cat.id)
        category.update_category('nature')
        category = Category.get_category_id(self.cat.id)
        self.assertTrue(category.name == 'nature')

class ImageTestClass(TestCase):
    # Set up Method
    def setUp(self):
        self.cat = Category(name="fashion")
        self.cat.save_category()

        self.loc = Location(name="urban")
        self.loc.save_location()

        self.image = Image(name='image test', description='my test',image_location=self.loc, image_category=self.cat)
        self.image.save_image()
    