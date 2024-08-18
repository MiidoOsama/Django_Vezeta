from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .models import Profile
from .forms import Login_Form , UserCreationForm
from django.contrib.auth import authenticate , login


def doctors_list (request):
    doctors = User.objects.all()
    context = {
        'doctors': doctors
    }

    return render (request , 'user/doctors_list.html' , context)


def doctors_detail(request, slug):
    doctors_detail = Profile.objects.get(slug=slug)
    context = {
        'doctors_detail'  : doctors_detail
    }
    return render(request , 'user/doctors_detail.html', context)


def user_login(request):
    if request.method == 'POST':
        form = Login_Form()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request , username = username , password = password)
        if user is not None:
            login(request,user)
            return redirect('accounts:doctors')
    else :
        form = Login_Form()

    context = {'form' : form}
    return render (request , 'user/login.html' , context)


def signup (request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            password= form.cleaned_data.get('password')
            user = authenticate(request, username= username, password=password)
            login(request,user)
            return redirect('accounts:doctors')
    else:
        form = UserCreationForm()
    context = {
        'form' : form
    }
    return render (request , 'user/signup.html' , context)