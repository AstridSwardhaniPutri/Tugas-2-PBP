Link Heroku:https://tugas-2-pbp-astrid.herokuapp.com/todolist/login/
1. Apa kegunaan {% csrf_token %} pada elemen <form>? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen <form>?
  CSRF token merupakan _alphanumeric_ kode yang merupaka secret value yang dibuat khusu pada suatu site. Setiap site memiliki token yang ebrbeda hal ini digunakan untuk mencegah adanya CSRF attack. Jika sebuah form tidak ada dalam elemen form maka form akan sulit diidentifikasi apakah user yang sama melakukan aksi yang diinginkan 
2. Apakah kita dapat membuat elemen <form> secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat <form> secara manual.
  Ya, kita bisa, hal ini dibuat dengan suatu file bernama forms.py, dalam file tersebut kita bisa mengkostumisasi secara mandiri bagaimana pembuatan forms, bagaimana data diambil dan disimpan, dll. Lalu, kita melakukan setup pada views.py untuk menghubungkan form pada forms.py untuk mengambil data dengan POST. Terakhir dengan melakukan setup pada html file pada folder template dengan memanggil kembali form tersebut.
3. Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
   data akan disimpan dalam form yang terdapat dalam views.py dengan form.save(). Lalu, data-data yang didapatkan disesuaikan oleh views.py dengan models.py yang selanjutnya akan ditampilkan pada html. 
4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
    a. Melakukan startapp todolist pada venv django
    b. Melakukan routing pada urls.py dalam todolist dan urls.py project django dalam urlpattern
    c. Menambahkan variabel-variabel yang dibutuhkan ke dalam models.py dengan tipe data yang dibutuhkan
    d. Membuat fungsi registrasi, login, logout, pada views.py
    e. Membuat html baru, todolist.html, untuk membuat page baru untuk menampilkan table todolist
    f.  Membuat html baru, new_task.html, untuk menambah task baru
    g. Melakukan routing kembali terhadap fitur-fitur diatas dengan menambahkan mereka dalam urls.py dalam todolist urlspattern
    h. Lalu, dipush ke github dan akan langsung di deploy ke Heroku
    i. Dalam Open App Heroku, buat 2 akun pengguna dengan 3 dummy data 
        Akun dan password:
          1. Username: astrid
             Password: gjgVDmqZGxWA376
          2. Username: JohnDoe
             Password: HKX7u4V8kWdXbfQ
    
