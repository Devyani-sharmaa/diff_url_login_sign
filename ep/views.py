from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import requests
API_KEY = 'add98a6444e84b1a83e601b7965687ba'
# from .models import Order
# from django.core import serializers
# Create your views here.
from .forms import MyForm
# from .models import add_product
# def dashboard_with_pivot(request):
#     return render(request, 'home.html', {})


# def pivot_data(request):
#     dataset = Order.objects.all()
#     data = serializers.serialize('json', dataset)
#     return JsonResponse(data, safe=False)


@login_required(login_url='login')
def HomePage(request):
    url=f'https://newsapi.org/v2/everything?q=apple&from=2024-09-25&to=2024-09-25&sortBy=popularity&apiKey={API_KEY}'
    response=requests.get(url)
    data=response.json()
    articles=data['articles']

    context={
        'articles': articles
    }
    return render (request,'home.html',context)


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


def add_product(request):
    return render(request,"add_product.html")

def saveproduct(request):
    if request.method=="POST":
        product_name=request.POST.get("pname")
        price_description=request.POST.get("pdes")
        price=request.POST.get("price")
        data=add_product(product_name=product_name,price_description=price_description,price=price, old_price=old_price, rating=rating ,out_of=out_of,image1=image1,image2=image2,image3=image3)
    data.save()
    return redirect('add_product.html')