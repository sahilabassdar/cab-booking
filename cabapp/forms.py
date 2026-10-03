from django import forms
from django.contrib.auth.models import User
from .models import Booking, Driver


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        exclude = ['status']


class RegisterForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class DriverRegisterForm(forms.Form):

    username = forms.CharField(max_length=150)
    password = forms.CharField(
        widget=forms.PasswordInput
    )

    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=15)

    car_type = forms.ChoiceField(
        choices=Driver.CAR_TYPES
    )

    vehicle_number = forms.CharField(max_length=20)

    def clean_username(self):
        username = self.cleaned_data['username']

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                "This username already exists."
            )

        return username