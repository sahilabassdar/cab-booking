from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('driver_login/', views.driver_login, name='driver_login'),  # ✅ ADD THIS
    path('driver/', views.driver_dashboard, name='driver_dashboard'),

    path('accept/<int:booking_id>/', views.accept_booking, name='accept_booking'),
    path('reject/<int:booking_id>/', views.reject_booking, name='reject_booking'),

    path('my-bookings/', views.my_bookings, name='my_bookings'),
]