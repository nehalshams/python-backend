from django.shortcuts import render

from home.models import Product
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

# Create your views here.

def index(request):
    # search = request.POST.get('search')
    if search:= request.POST.get('search'):
        query = SearchQuery(search)
        # vector = SearchVector('title', 'description', 'category', 'brand')
        vector = SearchVector('title', weight='A') \
        + SearchVector('description', weight='B') \
        + SearchVector('category', weight='C') \
        + SearchVector('brand', weight='D')
        rank = SearchRank(vector, query)
        products = Product.objects.annotate(
            rank = rank
        ).filter(rank__gt=0.05).order_by('-rank')
    else:
        products = Product.objects.all()
    context = {
        'products': products,
        'search': search,
    }
    for product in products:
        if search:
            print(product.title, product.rank)
    return render(request, 'index.html', context)