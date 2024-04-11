from django.urls import path
from . import views

urlpatterns = [
    # Homepage
    path('', views.home, name='home'),

    # Logout URL
    path('logout/', views.logout_user, name='logout'),

    # User Registration URL
    path('register/', views.register_user, name='register'),

    # Customer Record URL with Record ID
    path('record/<int:pk>', views.customer_record, name='record'),

    # Delete Record URL with Record ID
    path('delete_record/<int:pk>', views.delete_record, name='delete-record'),

    # Add Record URL
    path('add_record/', views.add_record, name='add-record'),

    # Update Record URL with Record ID
    path('update_record/<int:pk>', views.update_record, name='update-record'),
]
