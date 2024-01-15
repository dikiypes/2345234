from django.urls import path
from .views import CustomPasswordResetView, CustomLoginView, CustomLogoutView, register_user
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
]
