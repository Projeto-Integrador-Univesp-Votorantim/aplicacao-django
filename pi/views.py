from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm, RegistrationForm

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, 'index.html') # A modificar string de retorno 

def sobre_nos(request):
    return render(request, 'about-us.html')

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Replace 'home' with your desired URL after successful login
            else:
                error_message = "Usuário inválido."  # Error message for invalid login   
        else:
            error_message = "Preencha o formulário corretamente."  # Error message for invalid form
    else:
        form = LoginForm()
        error_message = None
    return render(request, 'login.html', {'form': form, 'error_message': error_message})

def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')
    else:
        form = RegistrationForm()
    
    return render(request, 'signup.html', {'form': form})