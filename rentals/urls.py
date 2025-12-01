from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('car/<int:pk>/', views.car_detail, name='car_detail'),
    path('success/', views.booking_success, name='booking_success'),
    
    # Auth routes
    path('login/', auth_views.LoginView.as_view(template_name='rentals/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='rentals/logout.html'), name='logout'),
    path('register/', views.register, name='register'),

]
