from django.shortcuts import render
from django.db.models import Q
from .models import Category, Recipe
from django.db.models import Count

def category_list(request):
    category_counts = Category.objects.annotate(recipe_count=Count('categories'))
    return render(request, 'category_list.html', {
        'categories': Category.objects.all(),
        'recipes': category_counts,
    })

def main(request):
    return render(request, 'main.html', {
        'recipes': Recipe.objects.order_by('-id')[:5],
    })
