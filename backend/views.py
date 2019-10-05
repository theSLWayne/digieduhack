from django.shortcuts import render
import json
import random

# Create your views here.
from backend.models import Article, User, Ingredient
from django.views import generic

def index(request):
    # articles = [ random.choice(Article.objects) for i in range(3) ]
    articles = []
    while len(articles) != 3:
        ar = random.choice(Article.objects.all())
        if ar not in articles:
            articles.append(ar)
    
    ingredients = []
    while len(ingredients) != 3:
        array = random.choice(Ingredient.objects.all())
        if array not in ingredients:
            ingredients.append(array)

    context = {
        'articles': articles,
        'ingredients': ingredients,
    }

    return render(request, 'index.html', context = context)

class ArticleListView(generic.ListView):
    model = Article
    #paginate_by = 10

class ArticleDetailView(generic.DetailView):
    model = Article

class IngredientListView(generic.ListView):
    model = Ingredient
    paginate_by = 20

class IngredientDetailView(generic.DetailView):
    model = Ingredient
