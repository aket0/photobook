from django.template import RequestContext
from django.shortcuts import render, redirect
from .forms import PhotoForm
from .models import Photo  

def index(request):
    return render(request, "index.html")

def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            for img in request.FILES.getlist('image'):
                Photo.objects.create(image=img)
            form.save()
            return redirect('success')
    else:
        form = PhotoForm()
    return render(request, 'upload.html', {'form': form})

def success(request):
    return render(request, 'success.html')

def home(request):
    photos = Photo.objects.all()
    return render(request, 'home.html', {'photos': photos})
