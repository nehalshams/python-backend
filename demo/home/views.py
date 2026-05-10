from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def root(request):
    return HttpResponse("Hello, World!")


def home(request):
    return HttpResponse("Welcome to the Home Page!")

# dynamic route with a parameter:
def dynamic_route(request, name):
    return HttpResponse(f"Hello, {name}! This is a dynamic route.")



# render a html template:
def product_detail(request, id):
    product_name = ["Mobile", "Laptop", "Tablet", "Headphones", "Camera"]
    context =  {
        'product_id': id, 
        'product_name': product_name[id],
        'products': product_name}
    return render(request, 'product_detail.html', context)


