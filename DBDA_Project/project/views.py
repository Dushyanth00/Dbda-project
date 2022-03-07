from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
	return render(request, 'project/home.html')


def register(request):
	if request.method == "POST":
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f'Hi {username}, your account is successfully created.')
			return redirect('Home')
	else:
		form = UserRegisterForm()

	return render(request, 'project/register.html', {'form': form})


@login_required()
def profile(request):
	return render(request, 'project/profile.html')


def settings(request):
	return render(request, 'project/settings.html')