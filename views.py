from django.shortcuts import render
from django.db.models import Q
from .models import Movie

def search_movies(request):
    """搜索电影视图"""
    query = request.GET.get('q', '')
    movies = []
    
    if query:
        # 搜索标题、描述和类型
        movies = Movie.objects.filter(
            Q(title__icontains=query) | 
            Q(description__icontains=query) |
            Q(genre__icontains=query)
        ).distinct()
    
    context = {
        'movies': movies,
        'query': query,
    }
    return render(request, 'movies/search.html', context)

def movie_detail(request, slug):
    """电影详情视图"""
    movie = Movie.objects.get(slug=slug)
    context = {
        'movie': movie,
    }
    return render(request, 'movies/detail.html', context)
