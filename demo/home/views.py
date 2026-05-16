from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentForm
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



def student_form(request):
    context = {  }
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        file = request.FILES.get('student_file')

        print(f"Received data - Name: {name}, Email: {email}, Age: {age}, File: {file}")
        if form.is_valid():
            form.save()
            context['success_message'] = "Student information saved successfully!"
        else:
            context['error_message'] = "There was an error saving the student information. Please check the form for errors."
    else:
        context['form'] = StudentForm()
    return render(request, 'student_form.html', context)
