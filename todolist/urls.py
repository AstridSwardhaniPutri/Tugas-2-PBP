from django.urls import path
from todolist.views import show_todolist, register, login_user, logout_user, create_task
from todolist.views import update_task, delete_task, get_todolist_json, add_todolist_item
from todolist.views import delete_todolist_item

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create-task'),
    path('update-task/<int:id>', update_task, name='update-task'),
    path('delete-task/<int:id>', delete_task, name='delete-task'),
    path('json/', get_todolist_json, name='get_todolist_json'),
    path('add/', add_todolist_item, name='add_todolist_item'),
    path('delete/<int:id>', delete_todolist_item, name='delete_todolist_item'),
]