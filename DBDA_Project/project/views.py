import os.path

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
from .models import Files
from django.http import HttpResponse
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
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


def models(request):
    context = {}
    context = {'file': Files.objects.all()}
    if request.method == "POST":
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
        return render(request, 'project/models.html')
    return render(request, 'project/models.html', context)


def searchbar(request):
    if request.method == "POST":
        searched = request.POST['searched']
        return render(request, 'project/searchbar.html', {'searched': searched})
    else:
        return render(request, 'project/searchbar.html')


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/adminupload")
            response['Content-Disposition'] = 'inline;filename=' + os.path.basename(file_path)
            return response

        raise Http404
