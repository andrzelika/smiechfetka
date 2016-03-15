from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

def post_list(request):
    # stworzenie zmiennej dla QuerySetu
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # metoda przyjmuje zapytanie i zwraca metodę render renderującą szablon html
    # przekazujemy QuerySet z listą posów do szablonu w zmiennej 'posts'
    return render(request, 'blog/post_list.html', {'posts': posts})
