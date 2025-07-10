
from django.contrib.auth.models import User
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login , logout
from .forms import User_Edit_Form
# Create your views here.
def SingIn(request):
    if request.user.is_authenticated:
        return redirect('home_app:homepage')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_app:homepage')
    return render(request, 'account_app/sing_in.html'  , {})





def SingUp(request):
    if request.user.is_authenticated:
        return render(request, 'home_app:homepage')
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        user = User.objects.create_user(username=username, email=email, password=password1, is_active=True)
        login(request, user)
        return redirect('home_app:homepage')
    return render(request , 'account_app/sing_up.html')


def Logout(request):
    logout(request)
    return redirect('home_app:homepage')


def Edit(request):
    user = request.user
    form = User_Edit_Form(instance=user)
    if request.method == 'POST':
        form = User_Edit_Form(instance=user, data=request.POST)
        if form.is_valid():
            form.save()

    return render(request , 'account_app/edit_user.html' , {'form':form})
