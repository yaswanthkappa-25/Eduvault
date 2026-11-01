from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

User=get_user_model()

def register_view(request):
    if request.method == "POST":
        email = request.POST.get("email", "").strip().lower()
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")

        if not email or not password or not confirm_password:
            messages.error(request, "Please fill in all fields.")
            return redirect("register")

        if User.objects.filter(email__iexact=email).exists():
            messages.error(request, "This email is already registered.")
            return redirect("register")

        if len(password) < 8:
            messages.error(request, "Password must contain at least 8 characters.")
            return redirect("register")

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("register")

        user = User.objects.create_user(
            username=email,
            email=email,
            password=password
        )

        messages.success(
            request,
            "Account created successfully! Please sign in."
        )
        return redirect("login")

    return render(request, "register.html")

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email", "").strip().lower()
        password = request.POST.get("password", "")

        user = authenticate(
            request,
            username=email,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect("dashboard")

        messages.error(request, "Invalid email or password.")
        return redirect("login")

    return render(request, "login.html")



@login_required(login_url="login")
def dashboard_view(request):
    return render(request, "dashboard.html")


@login_required(login_url="login")
def logout_view(request):
    if request.method == "POST":
        logout(request)
        messages.success(
            request,
            "You have logged out successfully."
        )
        return redirect("login")

    return redirect("dashboard")
def home(request):
    return render(request, "home.html")

