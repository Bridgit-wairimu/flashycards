from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import FlashCards
from django.views.generic import CreateView, ListView,DetailView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.from django.views.generic import ListView,DetailView,CreateView

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

@csrf_exempt
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
class FlashcardCreateView(LoginRequiredMixin,CreateView):
    model = FlashCards
    fields = ['images', 'title', 'description', 'category']
    template_name = 'post.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# <app>/<model>_<viewtype>.html
class FlashcardListView(ListView):
    model = FlashCards   
    template_name = 'index.html'   
    context_object_name = 'flashcards'
    ordering = ['-pub_date']

class FlashcardCreateView(CreateView):
    model = FlashCards
    template_name = 'post.html'   
    fields= ['title', 'description','category']    

class FlashcardUpdateView(UpdateView):
    model = FlashCards
    template_name = 'post.html'   
    fields= ['title', 'description','category']    

class FlashcardDeleteView(DeleteView):
    model = FlashCards
    template_name = 'delete.html'
    success_url = ('/')

def deleteForm(request):
    context ={     
    }
    return render(request ,'delete.html', context )    

def search_cards(request):
    if 'cards' in request.GET and request.GET["cards"]:
        cards = request.GET.get("cards")
        searched_images = Image.filter_by_location(cards)
        message = f"{cards}"
        print("Image.......",searched_images)
        return render(request, 'cards.html', {"message": message, "images": searched_images})
    else:
        message = "You haven't searched for any image"
        return render(request, 'cards.html', {"message": message})


