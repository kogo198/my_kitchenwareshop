from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django import forms


# ---------------------------------------------------------------------------
# Extended signup form (adds first_name, last_name, email)
# ---------------------------------------------------------------------------
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name  = forms.CharField(max_length=30, required=False)
    email      = forms.EmailField(required=False)

    class Meta(UserCreationForm.Meta):
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


# ---------------------------------------------------------------------------
# Main shop / home page
# ---------------------------------------------------------------------------
def shop(request):
    return render(request, 'shop.html')


# ---------------------------------------------------------------------------
# Authentication
# ---------------------------------------------------------------------------
def login_view(request):
    if request.user.is_authenticated:
        return redirect('shop')

    form = AuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.get_user()
        login(request, user)
        messages.success(request, f'Welcome back, {user.first_name or user.username}! 🎉')
        return redirect(request.GET.get('next', 'shop'))

    return render(request, 'login.html', {'form': form})


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('shop')

    form = SignUpForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, f'Welcome to KitchenCraft, {user.first_name or user.username}! 🎉')
        return redirect('shop')

    return render(request, 'signup.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('shop')


# ---------------------------------------------------------------------------
# Static pages
# ---------------------------------------------------------------------------
def products(request):
    return render(request, 'products.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


# ---------------------------------------------------------------------------
# Hostel views (kept from original urls – not used in main shop navigation)
# ---------------------------------------------------------------------------
def hostels(request):
    return render(request, 'hostels.html')


def add_hostel(request):
    return render(request, 'add_hostel.html')


@login_required(login_url='login')
def payment(request):
    return render(request, 'payment.html')


# ---------------------------------------------------------------------------
# API
# ---------------------------------------------------------------------------
def api_hostels(request):
    return JsonResponse({'hostels': []})
