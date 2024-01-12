from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from datetime import datetime

from base.forms import HistForm
from base.models import Contact, History
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from base.models import Shape

# Create your views here.
def index(request):
    stan = Shape.objects.all()
    #return HttpResponse("This is the home page.")
    return render(request, 'index.html', {'stan':stan})

def aboutUs(request):
    return render(request, 'about_us.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name') #Here, in request.POST.get('name'), 'name' is the name of the input type in contact.html that we insert in the html form!
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name = name, email = email, phone = phone, desc = desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Form successfully submitted')    #For viewing the message as a success alert message in contact.html. Since contact.html extends base.html so the code will be executed in base.html!
    return render(request, 'contact.html')

def handle_signup(request):
    if request.method == "POST":
        #Get the POST parameters!
        username = request.POST.get('username')
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        email = request.POST.get('email')
        password1 = request.POST.get('pass1')
        password2 = request.POST.get('pass2')

        #Check for erroneous inputs!
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
            return redirect("/")

        if not username.isalnum():  #username should be of alphanumeric characters!
            messages.error(request, "Username must be alphanumeric!")
            return redirect('/')

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect("/")

        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()
        messages.success(request, "Signed up successfully")
        return redirect("/")

    else:
        return HttpResponse("Not Allowed")
    
def handle_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(username = username, password = password)
        if user is not None:    #If the password or username is wrong, it would mean that user will be None
            login(request, user)
            messages.success(request, "Successfully logged in")
            return redirect('/')
        messages.error(request, "Invalid username or password!")
        return redirect('/')
    return HttpResponse('Not Allowed!')
    
def handle_logout(request):
    
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')

def news(request):
    return render(request, 'news.html')

def purchase_page(request):
    error = ''
    if request.method == 'POST':
        form = HistForm(request.POST)
        if form.is_valid():
            form.save()
            # После сохранения нового заказа, обновите список заказов
            orders = History.objects.all()
            return render(request, 'purchase_page.html', {'form': form, 'orders': orders})  # Передача переменной orders в контекст
        else:
            error = 'ВАШ ЗАКАЗ БЫЛ ЗАПОЛНЕН НЕВЕРНО'
    else:
        form = HistForm()
    orders = History.objects.all()
    data = {
        'form': form,
        'orders': orders,
        'error': error
    }

    return render(request, 'purchase_page.html', data)

def lscab(request):
    orders = History.objects.all()
    data = {
        'orders': orders
    }
    return render(request, 'lscab.html',data)
def historyc(request):
    return render(request, 'history.html')

def pageNotFound(request,exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")