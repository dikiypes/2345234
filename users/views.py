from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView
from django.contrib.auth import login
from .forms import UserForm


class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'


class CustomLoginView(LoginView):
    template_name = 'register/login.html'


class CustomLogoutView(LogoutView):
    next_page = 'catalog:home'  # Замените на ваш путь


def register_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('catalog:home')
    else:
        form = UserForm()

    return render(request, 'registration/register.html', {'form': form})
