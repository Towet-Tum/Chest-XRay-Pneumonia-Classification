from django.shortcuts import render, redirect
from cnnClassifier.pipeline.predictions import PredictionPipeline
from django.core.files.storage import FileSystemStorage
media = 'media'
import os 
from chest.models import  Diagnosis
from chest.forms import UserFormModel


from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


# Create your views here.

def index(request, id):
    user = User.objects.get(id=id)
    
    if request.method == 'POST' and request.FILES['upload']:
        f = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(f.name,f)
        file_url = fss.url(file)
        pred_img = os.path.join(media, file)
        pred = PredictionPipeline(pred_img)
        result = pred.predict()

       
        
        diagnosis = Diagnosis.objects.create(user=user, image=f, results=result)
        diagnosis.save()
        results = Diagnosis.objects.all()



        context = {
            'file_url':file_url,
            'results':results,
            'pred_img':pred_img

        }
        return render(request, 'index.html', context)
        
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserFormModel(request.POST)
        if form.is_valid():
            password = make_password(form.cleaned_data['password'])
            user = User.objects.create(username=form.cleaned_data['username'], first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'], email =form.cleaned_data['email'], password=password)
            user.save()
            
            return redirect('/user_login/')
    else:
        form = UserFormModel()
    return render(request, "register.html")

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/login_success/')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

def login_success(request):
    return render(request, 'success.html')
        