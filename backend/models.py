from django.db import models
from django.urls import reverse

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length = 100, help_text = "Enter user name.")
    email = models.EmailField(help_text = "Enter email.")

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length = 100, help_text = "Enter ingredient name.")
    manufacturer = models.CharField(max_length = 100, help_text = "Enter manufacturer.")
    price = models.FloatField(help_text = "Enter price.")
    photo = models.ImageField(upload_to="gallery", null = True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ingredient-detail', args = [str(self.id)])

class Article(models.Model):
    title = models.CharField(max_length = 100, help_text = "Enter title")
    user = models.ForeignKey('User', on_delete = models.SET_NULL, null = True)
    description = models.TextField(help_text = "Enter description")
    ingredients = models.ManyToManyField(Ingredient, help_text = "Enter ingredients.")
    created_on = models.DateField(help_text = "Enter created date")
    photo = models.ImageField(upload_to="gallery", null = True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article-detail', args = [str(self.id)])


    
