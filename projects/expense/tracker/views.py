from django.shortcuts import redirect, render
from .models import Transaction
from django.db.models import Sum, Q
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/login/')
def index(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        amount = request.POST.get('amount')
    

        # check if the amount and description are not empty
        if description and amount:
            # Save the transaction to the database
            Transaction.objects.create(
                description = description, 
                amount = amount,
                created_by = request.user
                )
            
            return redirect('index')

    context = {
        'transactions': Transaction.objects.filter(created_by=request.user).order_by('-created_at'),
        'total_balance': Transaction.objects.filter(created_by=request.user).aggregate(total = Sum('amount'))['total'] or 0,
        'income': Transaction.objects.filter(created_by=request.user, amount__gt = 0).aggregate(total = Sum('amount'))['total'] or 0,
        'expenses': Transaction.objects.filter(created_by=request.user, amount__lt = 0).aggregate(total = Sum('amount'))['total'] or 0
    }
    
    return render(request, 'index.html', context)




def delete_transaction(request, id):
    if request.method == "DELETE":
        transaction = Transaction.objects.get(id=id)
        transaction.delete()

        return JsonResponse({
            "message": "Transaction deleted successfully"
        })
    
def sign_up(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(Q(email=email) | Q(username=username))
        if user_obj.exists():
            messages.error(request, "User with this email and username already exists")
            return redirect('sign_up')
            return JsonResponse({
                "message": "User with this email and username already exists"
            }, status=400)
        
        user = User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.save()
        messages.success(request, "User created successfully. Please log in.")

    return render(request, 'sign_up.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username=username)
        if not user_obj.exists():
            messages.error(request, "User with this username does not exist")
            return redirect('login_page')
            return JsonResponse({
                "message": "User with this username does not exist"
            }, status=400)
        
        user_authenticated = authenticate(username=username, password=password)
        if not user_authenticated:
            messages.error(request, "Invalid username or password")
            return redirect('login_page')
        
        login(request, user_authenticated)
        # messages.success(request, "Logged in successfully")
        return redirect('/')
        

    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('/login/')