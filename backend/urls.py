from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),
    path('articles/', views.ArticleListView.as_view(), name = 'articles'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name = 'article-detail'), 
    path('ingredients/', views.IngredientListView.as_view(), name = 'ingredients'),
    path('ingredient/<int:pk>', views.IngredientDetailView.as_view(), name = 'ingredient-detail'),
]