

from django.shortcuts import render
from django.http import JsonResponse

from .models import Store

# Create your views here.
def index(request):
    return JsonResponse({"message": "Hello, World!"})


def blocked(request):
    return JsonResponse({"message": "You have accessed the blocked path."})





def store_view(request):
    print(request.headers)

    store  = Store.objects.get(bmp_id = request.headers.get('bmp-id'))

    response = {
        'store_name': store.store_name,
        'bmp_id': store.bmp_id
    }

    return JsonResponse(response)