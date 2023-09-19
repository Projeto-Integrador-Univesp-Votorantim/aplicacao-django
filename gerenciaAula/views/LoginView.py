from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from gerenciaAula.forms import LoginForm
from gerenciaAula.views import *

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')  # Replace 'home' with your desired URL after successful login
            else:
                error_message = "Usuário inválido."  # Error message for invalid login   
        else:
            error_message = "Preencha o formulário corretamente."  # Error message for invalid form
    else:
        form = LoginForm()
        error_message = None
    return render(request, 'login/login.html', {'form': form, 'error_message': error_message}, status=200)