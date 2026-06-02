from django.shortcuts import render
from django.http import JsonResponse
from .script import get_imdb_news

# Create your views here.
def run_scrapper(request):
    get_imdb_news()
    return JsonResponse({
        "status": 200,
        "message": 'Scraper executed'
    })

def index(request):
    context = {
        
    }
    return render(request, 'index.html', context)