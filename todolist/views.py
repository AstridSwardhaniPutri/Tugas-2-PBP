from turtle import title
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from todolist.models import Task
import datetime

# Create your views here.
@login_required(login_url='/todolist/login/')

def show_todolist(request):
    todolist = Task.objects.all()

    context = {
        'task_list': todolist,
        'nama': 'Astrid',
    }

    return render(request, "todolist.html", context)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)
def create_task(request):
    form = UserCreationForm()

    if request.method == "POST":
        if form.is_valid():
            form.save()
            user=request.user
            date=datetime.date.today()
            title=request.POST.get("create_task")
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:show_todolist')
    
    context = {'form':form}
    return render(request, 'new_task.html', context)
def logout_user(request):
    logout(request)
    return redirect('todolist:login')

