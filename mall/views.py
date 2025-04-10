from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, Shop, Employee
def home(request):
    return render(request, 'index.html')
# ================= CUSTOMER VIEWS ===================
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers.html', {'customers': customers})



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

# ================= EMPLOYEE VIEWS ===================
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employees.html', {'employees': employees})

def add_employee(request):
    if request.method == "POST":
        name = request.POST['name']
        position = request.POST['position']
        salary = request.POST['salary']
        shop_id = request.POST['shop']
        shop = get_object_or_404(Shop, id=shop_id)
        Employee.objects.create(name=name, position=position, salary=salary, shop=shop)
        return redirect('employee_list')
    shops = Shop.objects.all()
    return render(request, 'add_employee.html', {'shops': shops})

def edit_employee(request, id):  # ✅ Accept 'id' as an argument
    employee = get_object_or_404(Employee, id=id)
    shops = Shop.objects.all()

    if request.method == "POST":
        employee.name = request.POST["name"]
        employee.position = request.POST["position"]
        employee.salary = request.POST["salary"]
        employee.shop_id = request.POST["shop"]
        employee.save()
        return redirect("/employees/")  # Redirect to the employee list after saving

    return render(request, "edit_employee.html", {"employee": employee, "shops": shops})

def delete_employee(request, id):  # ✅ Match the URL pattern parameter
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    return redirect('employee_list')  # Redirect to the employee list page
# ================= SHOP VIEWS ===================
def shop_list(request):
    shops = Shop.objects.all()
    return render(request, 'shops.html', {'shops': shops})

def add_shop(request):
    if request.method == "POST":
        name = request.POST['name']
        owner = request.POST['owner']
        category = request.POST['category']
        contact = request.POST['contact']
        rent = request.POST['rent']
        Shop.objects.create(name=name, owner=owner, category=category, contact=contact, rent=rent)
        return redirect('shop_list')
    return render(request, 'add_shop.html')

def edit_shop(request, id):  # ✅ Use 'id' instead of 'shop_id'
    shop = get_object_or_404(Shop, id=id)

    if request.method == 'POST':
        shop.name = request.POST['name']
        shop.owner = request.POST['owner']
        shop.category = request.POST['category']
        shop.contact = request.POST['contact']
        shop.rent = request.POST['rent']
        shop.save()
        return redirect('shop_list')  # Redirect to the shop list page

    return render(request, 'edit_shop.html', {'shop': shop})

def delete_shop(request, id):  # ✅ Use 'id' instead of 'shop_id'
    shop = get_object_or_404(Shop, id=id)
    shop.delete()
    return redirect('shop_list')  # Redirect to the shop list page