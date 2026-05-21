from django.shortcuts import redirect, render
from .models import Transaction
from django.db.models import Sum
from django.http import JsonResponse

# Create your views here.
def index(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        amount = request.POST.get('amount')
    

        # check if the amount and description are not empty
        if description and amount:
            # Save the transaction to the database
            Transaction.objects.create(
                description = description, 
                amount = amount
                )
            
            return redirect('index')

    context = {
        'transactions': Transaction.objects.all(),
        'total_balance': Transaction.objects.aggregate(total = Sum('amount'))['total'] or 0,
        'income': Transaction.objects.filter(amount__gt = 0).aggregate(total = Sum('amount'))['total'] or 0,
        'expenses': Transaction.objects.filter(amount__lt = 0).aggregate(total = Sum('amount'))['total'] or 0
    }
    
    return render(request, 'index.html', context)




def delete_transaction(request, id):
    if request.method == "DELETE":
        transaction = Transaction.objects.get(id=id)
        transaction.delete()

        return JsonResponse({
            "message": "Transaction deleted successfully"
        })