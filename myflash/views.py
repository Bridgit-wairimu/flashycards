from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import FlashCards

# Create your views here.

@login_required(login_url='login')
def index(request):
    context = {
        'flashcards': FlashCards.objects.all()
    }
    return render(request, 'index.html' , context)


@csrf_exempt
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form =CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
            
                messages.success(request,'Account was created successfully')
                return redirect('login')
        context = {'form': form}
        return render(request,'registration/register.html',  context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user = authenticate(request, username=username ,password=password)
            
            if user is not None:   
                login(request, user)
               
        context={}
        return render(request,'registration/login.html',  context)

def logoutUser(request):
    logout(request)
    return redirect('login')



