from django.core import serializers
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from todolist.models import Task
import datetime

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    username = request.user
    data_todolist = Task.objects.filter(user=request.user)

    context = {
        'nama': username,
        'list_todolist': data_todolist,
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
            response = redirect('todolist:show_todolist')
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = redirect('todolist:login')
    response.delete_cookie('last_login')
    return response

def create_task(request):
    if request.method == 'POST':
        task = Task()
        task.user = request.user
        task.date = str(datetime.date.today())
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.is_finished = False

        task.save()
        messages.success(request, 'Task baru telah berhasil ditambah!')
        return redirect('todolist:show_todolist')

    context = {}
    return render(request, 'create-task.html', context)

def update_task(request, id):
    task = Task.objects.get(id=id)
    if task.user == request.user:
        task.is_finished ^= True
    else:
        return redirect('todolist:show_todolist')
    
    task.save()
    messages.success(request, 'Status task telah berhasil diubah!')
    return redirect('todolist:show_todolist')

def delete_task(request, id):
    task = Task.objects.get(id=id)
    if task.user == request.user:
        task.delete()
    else:
        return redirect('todolist:show_todolist')

    messages.success(request, 'Task telah berhasil dihapus!')
    return redirect('todolist:show_todolist')

def get_todolist_json(request):
    todolist_item = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', todolist_item))

def add_todolist_item(request):
    if request.method == 'POST':
        task = Task()
        task.user = request.user
        task.date = str(datetime.date.today())
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.is_finished = False

        task.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def delete_todolist_item(request, id):
    task = Task.objects.get(id=id)
    if task.user == request.user:
        task.delete()
        return HttpResponse(b"DELETED", status=201)

    return HttpResponseNotFound()