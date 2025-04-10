from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, Shop, Employee
def home(request):
    return render(request, 'index.html')
# ================= CUSTOMER VIEWS ===================
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers.html', {'customers': customers})

