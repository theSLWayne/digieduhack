from django.shortcuts import render

# Create your views here.
from backend.models import Article, User, Ingredient
from django.views import generic

def index(request):
    num_articles = Article.objects.count()
    num_ingredients = Ingredient.objects.count()
    num_users = User.objects.count()

    context = {
        'num_articles': num_articles,
        'num_ingredients': num_ingredients,
        'num_users': num_users,
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
