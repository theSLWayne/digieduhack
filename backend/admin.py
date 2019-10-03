from django.contrib import admin

# Register your models here.
from backend.models import Article, Ingredient, User

admin.site.register(User)
admin.site.register(Ingredient)
admin.site.register(Article)
