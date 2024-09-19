from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
from .forms import MyForm


@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')


def LoginPage(request):
    form=MyForm()
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html',{'form':form})





def submit(request):
    if request.method == 'POST':
        form=MyForm(request.POST)
        if form.is_valid():
            name=request.POST['fullname']
            email=request.POST['email']
            print('success')
            print(name)
            print(email)
            return HttpResponse("Thankyou for submiting this form")
        else:
            print('fail')
    return redirect(login)


def LogoutPage(request):
    logout(request)
    return redirect('login')