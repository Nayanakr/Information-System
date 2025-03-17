from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, Shop, Employee
def home(request):
    return render(request, 'index.html')
# ================= CUSTOMER VIEWS ===================
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers.html', {'customers': customers})

def add_customer(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        purchases = request.POST['purchases']
        feedback = request.POST['feedback']
        Customer.objects.create(name=name, phone=phone, purchases=purchases, feedback=feedback)
        return redirect('customer_list')
    return render(request, 'add_customer.html')

def edit_customer(request, id):  # ✅ Ensure the function has 'id' as an argument
    customer = get_object_or_404(Customer, id=id)

    if request.method == "POST":
        customer.name = request.POST.get("name", customer.name)
        customer.phone = request.POST.get("phone", customer.phone)
        customer.purchases = request.POST.get("purchases", customer.purchases)
        customer.feedback = request.POST.get("feedback", customer.feedback)
        customer.save()
        return redirect("/customers/")  # Redirect back to the customer list

    return render(request, "edit_customer.html", {"customer": customer})

def delete_customer(request, customer_id):  # ✅ Use 'customer_id' to match the URL
    customer = get_object_or_404(Customer, id=customer_id)
    customer.delete()
    return redirect('/customers/')  # Redirect to customer list after deletion

