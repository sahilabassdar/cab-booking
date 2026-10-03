from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name='home'),

    # ---------------- USER ----------------
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),

    # ---------------- DRIVER ----------------
    path('driver_login/', views.driver_login, name='driver_login'),
    path('driver_register/', views.driver_register, name='driver_register'),
    path('driver/', views.driver_dashboard, name='driver_dashboard'),

    # ---------------- DRIVER ACTIONS ----------------
    path(
        'accept/<int:booking_id>/',
        views.accept_booking,
        name='accept_booking'
    ),

    path(
        'reject/<int:booking_id>/',
        views.reject_booking,
        name='reject_booking'
    ),

    path(
        'drop/<int:booking_id>/',
        views.drop_booking,
        name='drop_booking'
    ),

    # ---------------- USER BOOKINGS ----------------
    path(
        'my-bookings/',
        views.my_bookings,
        name='my_bookings'
    ),
]