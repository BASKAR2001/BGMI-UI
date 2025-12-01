from django.shortcuts import render,redirect # type: ignore
from app5.models import Register 
from app5.forms import RegisterForm
from django.contrib.auth.models import User # type: ignore
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html')
def login(request):

    if request.method=='POST':
        user=request.POST.get('email')
        pwd=request.POST.get('password')
        verify=Register.objects.all()
        print(user,pwd)
        for i in verify:
            if i.email==user and i.password==pwd:
                return render(request,'home.html')
        else:
            return HttpResponse("invalid id and password")

    return render(request,'login.html')
    
def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,'logout successfully')
    return redirect('/home')
        
    return render(request,'login.html')
def register (request):
    if request.method=='POST':

        form=RegisterForm(request.POST)
        POST=User()
        POST.fanme=request.POST['fname']
        POST.lanme=request.POST['lname']
        POST.email=request.POST['email']
        POST.password=request.POST['password']
        POST.repassword=request.POST['repassword']
        if form.is_valid():
            form.save()
            return redirect("/login")
        else:
            pass 
    else:
        form=RegisterForm()
    return render(request,'register.html',{'form':form})
def media(request):
    return render(request,'media.html')
def maps(request):
    return render(request,'maps.html')
def events(request):
    return render(request,'events.html')
def outfits(request):
    return render(request,'outfits.html')
def weapon_skin(request):
    return render(request,'weapon_skin.html')
def vehicle_skin(request):
    return render(request,'vehicle_skin.html')
def uc_purchase(request):
    return render(request,'uc_purchase.html')
def cart(request):
    return render(request,'cart.html')


    