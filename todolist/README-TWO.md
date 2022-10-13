 ## Jelaskan perbedaan antara asynchronous programming dengan synchronous programming. ##
 Asyncronous merupakan multi-thread yang berarti operations dan program bisa dijalankan secara bersamaan atau paralel. Sedangkan synchronous programming merupakan single-thread yang berarti hanya satu operation atau program yang bisa dijalankan pada satu waktu.
 
 
 ## Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini. ##
 Event-Driven Programming memiliki fokus pada events (melakukan hovering atau mouse click) yang berarti flow dari program akan bergantung pada events dari user. Dalam Event-Driven Programming entitas seperti object, services, dll berkomunikasi secara indirectly.
 
 
 ## Jelaskan penerapan asynchronous programming pada AJAX. ##
1. Sebelum melakukan code, kita menambah src https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js diantara tag script dalam html header
2. Lalu, code dapat ditambahkan dalam html body dimulai dengan tag <script>, bisa dengan menambahkan JQuery dan program akan menunggu events untuk diproses secara asynchronous
 
 ## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas. ##
 1. Menambahkan get_todolist_json, add_todolist_item, delete_todolist_item dalam views
 ```
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
 ```
 
 
 2. Melakukan routing fungsi-fungsi baru di views ke dalam urls.py
  ```
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
  ```
 3. Melakukan asynchronous programming untuk melakukan add task dalam todolist.html
  ```
 <script>
    async function getTodolist() {
      return fetch('/todolist/json/').then((res) => res.json())
    }
  
    async function refreshTodolist() {
          document.getElementById("title").value = ""
          document.getElementById("description").value = ""

          document.getElementById("daftar_todolist").innerHTML = ""
          const todolist = await getTodolist()
          let htmlString = ``
          todolist.forEach((item) => {
            htmlString += `\n<div class="card shadow-lg" style="margin: auto; width: 70%;">
            <div class="card-header text-white" style="background-color: #0f8e9a;">
                <div class="fw-bold">${item.fields.title}</div>
                <div style="text-align:right">${item.fields.date}</div>
            </div>
            <div class="card-body">
                <p class="card-text">${item.fields.description}</p>
                <br>`
            if(item.fields.is_finished == true) {
              htmlString += `\n<p class="card-text fw-bold">Selesai</p>`
            }
            else {
              htmlString += `\n<p class="card-text fw-bold">Belum Selesai</p>`
            }
            htmlString += `\n<br>
                <a href="update-task/${item.pk}" class="btn btn-success m-2">Ubah Status</a>
                <button class="btn btn-danger m-2" onclick="deleteTodolist(${item.pk})">Hapus</button>
            </div>
            </div>
            <br>`
          })
          
          document.getElementById("daftar_todolist").innerHTML = htmlString
    }
  
    function addTodolist() {
      fetch('/todolist/add/', {
            method: "POST",
            body: new FormData(document.querySelector('#form'))
        }).then(refreshTodolist)
      return false
    }

    function deleteTodolist(id) {
      fetch(`/todolist/delete/${id}`).then(refreshTodolist)
      return false
    }
  
    document.getElementById("submit").onclick = addTodolist
    refreshTodolist()
</script>
  ```
