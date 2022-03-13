from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('', views.home, name = 'Home'),
    path('register/', views.register, name = 'Register'),
    path('profile/', views.profile, name = 'Profile'),
    path('settings/', views.settings, name = 'Settings'),
    path('login/', auth_view.LoginView.as_view(template_name = 'project\login.html'), name = 'Login'),
    path('logout/', auth_view.LogoutView.as_view(template_name = 'project\logout.html'), name='Logout'),
    path('models/', views.models, name = 'Models'),
    path('search/', views.searchbar, name = 'SearchBar'),
]
