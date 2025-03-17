from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Customer URLs
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/add/', views.add_customer, name='add_customer'),
    path('customers/edit/<int:id>/', views.edit_customer, name='edit_customer'),
    path('customers/delete/<int:customer_id>/', views.delete_customer, name='delete_customer'),

   # Employee URLs
    path('employees/', views.employee_list, name='employee_list'),
    path('employees/add/', views.add_employee, name='add_employee'),
    path('employees/edit/<int:id>/', views.edit_employee, name='edit_employee'),
    path('employees/delete/<int:id>/', views.delete_employee, name='delete_employee'),
]
