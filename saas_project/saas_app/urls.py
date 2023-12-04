# saas_app/urls.py

from django.urls import path
from .views import employee_login, employee_register, admin_login, admin_panel

urlpatterns = [
    path('employee/login/', employee_login, name='employee_login'),
    path('employee/register/', employee_register, name='employee_register'),
    path('admin/login/', admin_login, name='admin_login'),
    path('admin/panel/', admin_panel, name='admin_panel'),
]
