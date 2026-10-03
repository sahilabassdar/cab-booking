
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import RegisterForm, BookingForm, DriverRegisterForm
from .models import Booking, Driver


# ---------------- REGISTER ----------------
def register(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            return redirect('login')

    else:
        form = RegisterForm()

    return render(
        request,
        'cabapp/register.html',
        {'form': form}
    )


# ---------------- DRIVER REGISTER --------------
def driver_register(request):

    if request.method == 'POST':

        form = DriverRegisterForm(request.POST)

        if form.is_valid():

            # Create login account
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )

            # Create driver profile
            Driver.objects.create(
                user=user,
                name=form.cleaned_data['name'],
                phone=form.cleaned_data['phone'],
                car_type=form.cleaned_data['car_type'],
                vehicle_number=form.cleaned_data['vehicle_number'],
                status='Available'
            )

            return redirect('driver_login')

    else:
        form = DriverRegisterForm()

    return render(
        request,
        'cabapp/driver_register.html',
        {'form': form}
    )

# ---------------- LOGIN ----------------
def user_login(request):

    error = ""

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('home')

        else:

            error = "Invalid username or password"

    return render(
        request,
        'cabapp/login.html',
        {'error': error}
    )


# ---------------- LOGOUT ----------------
def user_logout(request):

    logout(request)

    return redirect('login')


# ---------------- HOME (BOOK CAB) ----------------
def home(request):

    if not request.user.is_authenticated:
        return redirect('login')

    form = BookingForm()

    if request.method == 'POST':

        form = BookingForm(request.POST)

        if form.is_valid():

            booking = form.save(commit=False)

            booking.user = request.user
            booking.status = 'Pending'

            booking.save()

            return redirect('home')

    bookings = Booking.objects.filter(
        user=request.user
    ).order_by('-id')

    return render(
        request,
        'cabapp/home.html',
        {
            'form': form,
            'bookings': bookings
        }
    )


# ---------------- DRIVER LOGIN ----------------
def driver_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            try:

                driver = Driver.objects.get(user=user)

                request.session['driver'] = driver.id

                return redirect('driver_dashboard')

            except Driver.DoesNotExist:

                pass

    return render(
        request,
        'cabapp/driver_login.html'
    )


# ---------------- DRIVER DASHBOARD ----------------
def driver_dashboard(request):

    if not request.session.get('driver'):
        return redirect('driver_login')

    bookings = Booking.objects.all().order_by('-id')

    return render(
        request,
        'cabapp/driver_dashboard.html',
        {'bookings': bookings}
    )


# ---------------- ACCEPT BOOKING ----------------
def accept_booking(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id
    )

    booking.status = 'Assigned'

    booking.save()

    return redirect('driver_dashboard')


# ---------------- REJECT BOOKING ----------------
def reject_booking(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id
    )

    booking.status = 'Cancelled'

    booking.save()

    return redirect('driver_dashboard')


# ---------------- DROP / REACHED DESTINATION ----------------
def drop_booking(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id
    )

    booking.status = 'Reached Destination'

    booking.save()

    return redirect('driver_dashboard')


# ---------------- USER BOOKING STATUS ----------------
def my_bookings(request):

    if not request.user.is_authenticated:
        return redirect('login')

    bookings = Booking.objects.filter(
        user=request.user
    ).order_by('-id')

    return render(
        request,
        'cabapp/my_bookings.html',
        {'bookings': bookings}
    )

