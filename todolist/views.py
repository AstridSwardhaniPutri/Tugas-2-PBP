from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from todolist.models import Task
import datetime
from django.urls import reverse

# Create your views here.
@login_required(login_url='login/')

def show_todolist(request):
    user=get_user(request)
    todolist = Task.objects.filter(user=user)
    
    context = {
        'task_list': todolist,
        'nama': user,
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
    if request.method == "POST":
        date=datetime.datetime.now()
        title=request.POST.get("Task_Name")
        description=request.POST.get("Task_Description")
        user=request.user
        Task.objects.create(
            user=user,
            date=date,
            title=title,
            description=description,
            # is_finished=is_finished
        )
        return HttpResponseRedirect(reverse('todolist:show_todolist'))

    # context = {'form':form}
    return render(request, 'new_task.html')

def update_task (request,pk):
    task=Task.objects.filter(user=request.user).get(pk=pk)
    if(task.is_finished):
        task.is_finished=False
    else:
        task.is_finished=True
    task.save()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))
    
def delete_task (request,pk):
    task=Task.objects.filter(user=request.user).get(pk=pk)
    task.delete()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))

def logout_user(request):
    logout(request)
    return redirect('todolist:login')

